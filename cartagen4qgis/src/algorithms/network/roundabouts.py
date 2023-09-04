# -*- coding: utf-8 -*-

"""
/***************************************************************************
 CartAGen4QGIS
                                 A QGIS plugin
 Cartographic generalization
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-05-11
        copyright            : (C) 2023 by Guillaume Touya, Justin Berli
        email                : guillaume.touya@ign.fr
 ***************************************************************************/
"""

__author__ = 'Guillaume Touya, Justin Berli'
__date__ = '2023-05-11'
__copyright__ = '(C) 2023 by Guillaume Touya, Justin Berli'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing, QgsFeatureSink, QgsProcessingAlgorithm,
    QgsFeature, QgsGeometry, QgsProcessingParameterDefinition,
    QgsWkbTypes
)
from qgis.core import (
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
    QgsProcessingParameterBoolean,
    QgsProcessingParameterNumber,
    QgsProcessingParameterDistance,
)

from cartagen4py.utils.partitioning import *
from cartagen4py.data_enrichment import is_roundabout

from cartagen4qgis import PLUGIN_ICON
from cartagen4qgis.src.tools import *

import geopandas
from shapely import Polygon
from shapely.wkt import loads

class DetectRoundaboutsQGIS(QgsProcessingAlgorithm):
    """
    Detect roundabouts
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    AREA = 'AREA'
    MILLER = 'MILLER'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input road network'),
                [QgsProcessing.TypeVectorLine]
            )
        )
        
        self.addParameter(
                QgsProcessingParameterNumber(
                self.AREA,
                self.tr('Maximum area'),
                type=QgsProcessingParameterNumber.Integer,
                defaultValue=40000,
                optional=False
            )
        )

        miller = QgsProcessingParameterNumber(
            self.MILLER,
            self.tr('Minimum Miller index'),
            type=QgsProcessingParameterNumber.Double,
            defaultValue=0.95,
            optional=False
        )
        miller.setFlags(miller.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        self.addParameter(miller)

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Roundabouts')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        # Get the QGIS source from the parameters
        source = self.parameterAsSource(parameters, self.INPUT, context)

        # Convert the source to GeoDataFrame, get the list of records and the number of entities
        gdf = qgis_source_to_geodataframe(source)
        records = gdf.to_dict('records')
        count = len(records)

        # Define the output sink
        (sink, dest_id) = self.parameterAsSink(
            parameters, self.OUTPUT, context,
            fields=source.fields(),
            geometryType=QgsWkbTypes.Polygon,
            crs=source.sourceCrs()
        )

        # Compute the number of steps to display within the progress bar and
        total = 100.0 / count if count > 0 else 0
        
        # Retrieve parameters
        area = self.parameterAsInt(parameters, self.AREA, context)
        miller = self.parameterAsDouble(parameters, self.MILLER, context)

        # Actual algorithm
        roads = []
        for road in records:
            roads.append(road['geometry'])

        faces = calculate_network_faces(roads, convex_hull=False)

        roundabouts = []
        index = 0
        for current, face in enumerate(faces):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            add, infos = is_roundabout(face, area, miller)
            if add:
                infos['cid'] = index
                roundabouts.append(infos)
                index += 1

            # Update the progress bar
            feedback.setProgress(int(current * total))

        # Converts the list of dicts to a list of qgis features
        result = list_to_qgis_feature(roundabouts)

        sink.addFeatures(result, QgsFeatureSink.FastInsert)

        # # Add a feature in the sink
        # sink.addFeature(result, QgsFeatureSink.FastInsert)

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {
            self.OUTPUT: dest_id
        }

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Detect roundabouts'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Network'

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return PLUGIN_ICON

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return DetectRoundaboutsQGIS()