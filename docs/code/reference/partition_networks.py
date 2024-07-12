from matplotlib import pyplot as plt
from matplotlib import colormaps
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from shapely.wkt import loads
import cartagen4py as c4

points = [
    loads('POINT (-185202.41308318282 5371228.815927938)'), 
    loads('POINT (-184905.65881061598 5371437.875006501)'), 
    loads('POINT (-184899.3948681871 5371397.1593807135)'), 
    loads('POINT (-185023.89072396056 5371370.537625391)'), 
    loads('POINT (-185041.8995584435 5371371.3206181945)'), 
    loads('POINT (-185037.20160162187 5371351.745798104)'), 
    loads('POINT (-185024.67371676414 5371310.247179513)'), 
    loads('POINT (-185026.23970237136 5371282.842431387)'), 
    loads('POINT (-185105.32197553563 5371306.332215495)'), 
    loads('POINT (-185012.92882471005 5371564.719840685)'), 
    loads('POINT (-184963.60027808286 5371628.142257777)'), 
    loads('POINT (-184778.8139764317 5371505.995380415)'), 
    loads('POINT (-184827.35953025531 5371400.291351927)'), 
    loads('POINT (-185322.99397493823 5371238.211841581)'), 
    loads('POINT (-185322.21098213462 5371317.294114745)'), 
    loads('POINT (-185185.1872415035 5371407.338287161)'), 
    loads('POINT (-185179.70629187825 5371417.517193607)'), 
    loads('POINT (-185169.52738543137 5371405.772301553)'), 
    loads('POINT (-185167.17840702055 5371435.52602809)'), 
]

network = [
    loads('LINESTRING (-184725.60487070138 5371469.550111022, -184736.4880665912 5371458.136987171)'), 
    loads('LINESTRING (-185104.42037080176 5371511.138502412, -185096.57086660343 5371519.466753214, -185078.89936393482 5371538.21599815, -185078.78541178408 5371538.336899722, -185056.82308049666 5371560.859070892, -185009.7710752708 5371609.110094479, -185007.80618184607 5371611.383549916, -184999.15683981692 5371621.391151012, -184985.70263493745 5371636.958112258, -184982.9834646192 5371640.104276624)'), 
    loads('LINESTRING (-184956.32695577687 5371446.75698532, -184939.6899034541 5371411.850899637, -184913.46908673336 5371361.361652138, -184911.62969890685 5371358.157581968)'), 
    loads('LINESTRING (-184875.47284854745 5371540.732933849, -184883.6324941358 5371567.169046774, -184884.45068495173 5371581.0637440905, -184887.98333952547 5371643.391921453)'), 
    loads('LINESTRING (-184946.6100944189 5371650.821013643, -184944.25179108567 5371608.440687273, -184941.56716193075 5371581.541712855)'), 
    loads('LINESTRING (-184776.0322122919 5371550.356978994, -184769.03046891367 5371541.246599238, -184757.94506006458 5371518.84936812, -184742.60086886465 5371491.8729209965, -184730.17024731488 5371474.663391207, -184725.60487070138 5371469.550111022)'), 
    loads('LINESTRING (-184866.5945948691 5371389.956665693, -184873.3588861456 5371385.690154516, -184911.62969890685 5371358.157581968)'), 
    loads('LINESTRING (-185056.49942681778 5371295.449631062, -185064.20015478972 5371295.406926281, -185074.20691274264 5371294.813263079, -185087.5427086721 5371290.018705619, -185109.80273711224 5371277.930331787, -185114.22097502518 5371275.873578137)'), 
    loads('LINESTRING (-185044.91660725433 5371255.274801716, -185053.42493728004 5371287.625271775, -185056.49942681778 5371295.449631062)'), 
    loads('LINESTRING (-185114.22097502518 5371275.873578137, -185121.74640789523 5371310.215058748, -185122.20025266343 5371317.9188114405, -185119.71731325684 5371320.136848678, -185107.31673195696 5371324.461838894, -185072.09817553553 5371336.076623527)'), 
    loads('LINESTRING (-185097.6920014813 5371417.93967189, -185145.62692138483 5371405.017981575)'), 
    loads('LINESTRING (-185002.40768763862 5371348.631783701, -185003.86694972194 5371347.716932534, -185031.0128130795 5371332.163766921, -185064.09282452168 5371314.601919641)'), 
    loads('LINESTRING (-185002.40768763862 5371348.631783701, -184972.5072509364 5371289.388249507)'), 
    loads('LINESTRING (-185013.43390491544 5371416.726031476, -185018.22296293126 5371413.957055943, -185039.09571402887 5371399.328077525, -185058.65499559935 5371388.090165353, -185082.04436729394 5371376.486942387, -185085.43895500162 5371375.7333534965)'), 
    loads('LINESTRING (-185013.43390491544 5371416.726031476, -184999.3869914133 5371388.430913974, -184983.63039039288 5371359.132894597)'), 
    loads('LINESTRING (-184965.53478683293 5371327.488823438, -184911.62969890685 5371358.157581968)'), 
    loads('LINESTRING (-184841.18488360877 5371355.570884195, -184857.19706981847 5371347.166742999, -184891.9548416533 5371330.058236988, -184895.16374307786 5371328.487450676)'), 
    loads('LINESTRING (-184863.08532470846 5371384.0906299045, -184841.18488360877 5371355.570884195)'), 
    loads('LINESTRING (-185097.6920014813 5371417.93967189, -185107.45200441818 5371455.186241745)'), 
    loads('LINESTRING (-185117.350559607 5371497.118463983, -185124.58139771514 5371489.096657331, -185133.53727199754 5371480.7785131475, -185139.18892061617 5371475.529298473, -185159.69019293005 5371459.265367386)'), 
    loads('LINESTRING (-185104.42037080176 5371511.138502412, -185086.66382880096 5371510.9495263705, -185074.8092442736 5371508.201558107, -185052.35814680977 5371503.045095394, -185043.26953530544 5371500.547150403, -185033.28685136637 5371501.553501995, -185004.13829860254 5371508.804636296)'), 
    loads('LINESTRING (-184906.49241911544 5371474.147536484, -184898.98897337518 5371458.85484115, -184868.49130415558 5371396.470530056, -184866.5945948691 5371389.956665693)'), 
    loads('LINESTRING (-184990.43073186307 5371511.964605021, -184936.7530930223 5371523.155397806)'), 
    loads('LINESTRING (-184917.3361615667 5371466.739958805, -184935.96981464827 5371519.198378438, -184936.7530930223 5371523.155397806)'), 
    loads('LINESTRING (-184736.4880665912 5371458.136987171, -184748.71715768572 5371443.883074327, -184770.99303307265 5371427.376884487, -184780.8037674814 5371416.441488997, -184784.3585641607 5371411.398994563)'), 
    loads('LINESTRING (-184825.45818558556 5371530.03180713, -184829.5700506031 5371527.441113838, -184849.0974819549 5371515.653225886, -184877.88849157872 5371497.655869943, -184882.00779554516 5371492.855911524)'), 
    loads('LINESTRING (-184939.9691712774 5371547.399698471, -184944.92035972624 5371547.382137743, -184986.62662203162 5371547.807435527, -184990.35150708718 5371545.6537676575, -184990.43073186307 5371511.964605021)'), 
    loads('LINESTRING (-184941.56716193075 5371581.541712855, -184995.93255106008 5371577.350682862)'), 
    loads('LINESTRING (-184875.47284854745 5371540.732933849, -184865.49882753962 5371544.22350248, -184836.56059944932 5371555.050958757)'), 
    loads('LINESTRING (-184776.0322122919 5371550.356978994, -184795.14163419767 5371543.149658851, -184812.25148025868 5371537.027226885, -184824.659988871 5371530.493291637, -184825.45818558556 5371530.03180713)'), 
    loads('LINESTRING (-184836.56059944932 5371555.050958757, -184845.84921116626 5371581.972403162, -184807.52678899115 5371601.639402794, -184801.15735286687 5371605.606437842)'), 
    loads('LINESTRING (-184887.98333952547 5371643.391921453, -184823.7474023712 5371648.167595626, -184820.91722584935 5371649.163735945)'), 
    loads('LINESTRING (-184836.56059944932 5371555.050958757, -184809.38069638066 5371567.706787168, -184788.20748766675 5371577.245352337)'), 
    loads('LINESTRING (-184982.9834646192 5371640.104276624, -184978.09025504737 5371645.778583417, -184976.8021529034 5371646.272422283, -184972.97827553618 5371647.738437715, -184959.6169180738 5371649.7734352, -184946.6100944189 5371650.821013643)'), 
    loads('LINESTRING (-184946.6100944189 5371650.821013643, -184906.04926902373 5371653.502775688, -184899.0006099802 5371650.607541412, -184887.98333952547 5371643.391921453)'), 
    loads('LINESTRING (-185082.86628013416 5371236.3197572855, -185111.67418670698 5371225.637574483)'), 
    loads('LINESTRING (-185044.91660725433 5371255.274801716, -185066.51552639788 5371243.639942857)'), 
    loads('LINESTRING (-185066.51552639788 5371243.639942857, -185073.57807543923 5371239.769780514, -185082.86628013416 5371236.3197572855)'), 
    loads('LINESTRING (-185056.49942681778 5371295.449631062, -185064.09282452168 5371314.601919641)'), 
    loads('LINESTRING (-185019.51994724196 5371267.82513925, -185023.13193593788 5371266.0923559815, -185044.91660725433 5371255.274801716)'), 
    loads('LINESTRING (-184986.85059964538 5371283.015567933, -184999.04118126715 5371277.460800597, -185019.51994724196 5371267.82513925)'), 
    loads('LINESTRING (-184972.5072509364 5371289.388249507, -184986.85059964538 5371283.015567933)'), 
    loads('LINESTRING (-184962.46939034373 5371294.12506212, -184972.5072509364 5371289.388249507)'), 
    loads('LINESTRING (-184941.89392963462 5371304.456584128, -184951.37539510944 5371299.614744785)'), 
    loads('LINESTRING (-184951.37539510944 5371299.614744785, -184961.92917636188 5371294.2951517645, -184962.46939034373 5371294.12506212)'), 
    loads('LINESTRING (-185064.09282452168 5371314.601919641, -185064.90787613916 5371316.762331502, -185072.09817553553 5371336.076623527)'), 
    loads('LINESTRING (-185072.09817553553 5371336.076623527, -185077.48079110764 5371350.390406717)'), 
    loads('LINESTRING (-185077.48079110764 5371350.390406717, -185080.28116416524 5371358.231078069, -185085.43895500162 5371375.7333534965)'), 
    loads('LINESTRING (-185085.43895500162 5371375.7333534965, -185096.82020398218 5371414.816258245, -185097.6920014813 5371417.93967189)'), 
    loads('LINESTRING (-184965.53478683293 5371327.488823438, -184953.11011297084 5371303.377184048, -184951.37539510944 5371299.614744785)'), 
    loads('LINESTRING (-184983.63039039288 5371359.132894597, -185002.40768763862 5371348.631783701)'), 
    loads('LINESTRING (-184983.63039039288 5371359.132894597, -184983.00915038498 5371357.927308481, -184965.53478683293 5371327.488823438)'), 
    loads('LINESTRING (-184913.8445066714 5371318.682531984, -184920.12521297488 5371315.549076507, -184941.89392963462 5371304.456584128)'), 
    loads('LINESTRING (-184895.16374307786 5371328.487450676, -184913.8445066714 5371318.682531984)'), 
    loads('LINESTRING (-184911.62969890685 5371358.157581968, -184906.94212362941 5371348.634164567, -184895.16374307786 5371328.487450676)'), 
    loads('LINESTRING (-184866.5945948691 5371389.956665693, -184863.08532470846 5371384.0906299045)'), 
    loads('LINESTRING (-184808.56594841028 5371380.973362457, -184817.04689430672 5371373.1538956575, -184829.49443339335 5371362.6143429, -184841.18488360877 5371355.570884195)'), 
    loads('LINESTRING (-184784.3585641607 5371411.398994563, -184791.17778517748 5371401.055128867, -184805.30092694785 5371383.927938416, -184808.56594841028 5371380.973362457)'), 
    loads('LINESTRING (-185145.62692138483 5371405.017981575, -185155.5728235805 5371443.081723806)'), 
    loads('LINESTRING (-185155.5728235805 5371443.081723806, -185157.47819112672 5371450.570924534, -185159.69019293005 5371459.265367386)'), 
    loads('LINESTRING (-185107.45200441818 5371455.186241745, -185155.5728235805 5371443.081723806)'), 
    loads('LINESTRING (-185107.45200441818 5371455.186241745, -185110.6407530911 5371467.283513122, -185117.350559607 5371497.118463983)'), 
    loads('LINESTRING (-185117.350559607 5371497.118463983, -185113.09429965928 5371501.926668634, -185104.42037080176 5371511.138502412)'), 
    loads('LINESTRING (-184978.78135641917 5371435.62358369, -184994.55180480098 5371427.785653402, -185013.43390491544 5371416.726031476)'), 
    loads('LINESTRING (-184956.32695577687 5371446.75698532, -184978.78135641917 5371435.62358369)'), 
    loads('LINESTRING (-185004.13829860254 5371508.804636296, -184994.23662644112 5371511.186645957, -184990.43073186307 5371511.964605021)'), 
    loads('LINESTRING (-184956.32695577687 5371446.75698532, -184920.10955913892 5371464.780821005, -184917.3361615667 5371466.739958805)'), 
    loads('LINESTRING (-184917.3361615667 5371466.739958805, -184906.49241911544 5371474.147536484)'), 
    loads('LINESTRING (-184936.7530930223 5371523.155397806, -184935.25328669732 5371523.382403699, -184918.97350862328 5371527.247026613, -184897.43660267 5371532.941965236)'), 
    loads('LINESTRING (-184882.00779554516 5371492.855911524, -184883.16052652113 5371491.407044915, -184886.90908295882 5371487.319326026, -184896.31786610463 5371481.239318131, -184906.49241911544 5371474.147536484)'), 
    loads('LINESTRING (-184897.43660267 5371532.941965236, -184882.00779554516 5371492.855911524)'), 
    loads('LINESTRING (-184897.43660267 5371532.941965236, -184897.03345554217 5371533.103925542, -184875.47284854745 5371540.732933849)'), 
    loads('LINESTRING (-184939.9691712774 5371547.399698471, -184939.63699986954 5371541.75929766, -184936.7530930223 5371523.155397806)'), 
    loads('LINESTRING (-184941.56716193075 5371581.541712855, -184940.62119356176 5371572.486402055, -184939.9691712774 5371547.399698471)'), 
    loads('LINESTRING (-184788.20748766675 5371577.245352337, -184776.0322122919 5371550.356978994)'), 
    loads('LINESTRING (-184820.91722584935 5371649.163735945, -184816.626988496 5371639.588053486, -184815.37407389042 5371636.791582896, -184801.15735286687 5371605.606437842)'), 
    loads('LINESTRING (-184801.15735286687 5371605.606437842, -184788.20748766675 5371577.245352337)'), 
    loads('LINESTRING (-185210.92892606626 5371385.681536197, -185196.7872615506 5371339.446121639, -185184.8411408317 5371300.121081746, -185172.28795219414 5371252.825501085)'), 
    loads('LINESTRING (-185145.62692138483 5371405.017981575, -185151.99676094082 5371403.397581355, -185195.30321639444 5371391.302459515, -185208.2602750012 5371387.082341728, -185210.92892606626 5371385.681536197)'), 
    loads('LINESTRING (-185401.20493015027 5371278.85858006, -185403.98626992386 5371277.036896677, -185407.01666770835 5371272.4394773645, -185402.1081290761 5371254.508622282, -185390.6129824465 5371215.847652732)'), 
    loads('LINESTRING (-185164.243655223 5371209.680098655, -185169.92796315614 5371208.100389911, -185203.40440364293 5371197.278952045, -185207.14585706653 5371196.058597421, -185215.8209704927 5371193.229017832)'), 
    loads('LINESTRING (-185246.69128494666 5371203.545087896, -185254.3197051505 5371204.610873019, -185265.49665747272 5371207.536746478, -185274.69041655635 5371211.822727029, -185285.96466681684 5371216.3993608905)'), 
    loads('LINESTRING (-185259.55504311871 5371263.1080795, -185253.97025642887 5371247.702157137, -185243.9901677688 5371230.072264491, -185240.97205966376 5371222.506962529, -185240.9236408595 5371222.385594094, -185239.63247323336 5371219.149102965, -185236.44508861995 5371211.74570605, -185232.1198364186 5371201.372823955)'), 
    loads('LINESTRING (-185341.62807085045 5371269.280603303, -185336.69116537005 5371288.2100586, -185332.42266634185 5371304.476965377, -185335.298476488 5371320.595935468)'), 
    loads('LINESTRING (-185341.62807085045 5371269.280603303, -185344.41979077447 5371274.636790063, -185358.42784761445 5371304.58992818)'), 
    loads('LINESTRING (-185316.9262595013 5371335.629305901, -185314.5612429166 5371328.177022597, -185313.98824865662 5371326.470331046, -185303.38256389636 5371294.880711192, -185299.78454506004 5371264.171625445, -185298.89647704054 5371260.773153941)'), 
    loads('LINESTRING (-185259.55504311871 5371263.1080795, -185265.63215041204 5371279.865282142, -185275.6057040124 5371302.051219592, -185278.90812338216 5371316.07415753, -185286.51160658718 5371340.057422275, -185288.29511729334 5371344.645216249, -185288.66179120482 5371345.632908081, -185292.0559732729 5371354.775646643)'), 
    loads('LINESTRING (-185258.6623039958 5371374.013654168, -185272.74837278193 5371370.278636888, -185276.83571146434 5371367.2750771325, -185283.2364512198 5371361.511287911, -185292.0559732729 5371354.775646643)'), 
    loads('LINESTRING (-185111.67418670698 5371225.637574483, -185164.243655223 5371209.680098655)'), 
    loads('LINESTRING (-185114.22097502518 5371275.873578137, -185135.74761117905 5371265.347184668, -185172.28795219414 5371252.825501085)'), 
    loads('LINESTRING (-185210.92892606626 5371385.681536197, -185218.2629968348 5371414.682420135, -185218.46149335487 5371415.467327224)'), 
    loads('LINESTRING (-185159.69019293005 5371459.265367386, -185169.4127389971 5371451.509854103, -185202.64451211225 5371427.090175658, -185218.46149335487 5371415.467327224)'), 
    loads('LINESTRING (-185371.6889594479 5371219.179765679, -185385.17853863788 5371216.99853578, -185390.6129824465 5371215.847652732)'), 
    loads('LINESTRING (-185364.19834948741 5371220.452691471, -185370.73752568424 5371219.374290199, -185371.6889594479 5371219.179765679)'), 
    loads('LINESTRING (-185382.33982812922 5371290.193999024, -185389.2570889189 5371286.194132777, -185401.20493015027 5371278.85858006)'), 
    loads('LINESTRING (-185355.4821480471 5371221.936407568, -185364.19834948741 5371220.452691471)'), 
    loads('LINESTRING (-185330.81630599458 5371223.538559814, -185347.16906839274 5371223.258139876, -185355.4821480471 5371221.936407568)'), 
    loads('LINESTRING (-185285.96466681684 5371216.3993608905, -185298.1100360464 5371221.752559795, -185315.56827019237 5371223.891425433, -185330.81630599458 5371223.538559814)'), 
    loads('LINESTRING (-185295.81219471473 5371248.1178331785, -185291.97693651865 5371232.05593233, -185285.96466681684 5371216.3993608905)'), 
    loads('LINESTRING (-185355.4821480471 5371221.936407568, -185346.67770961806 5371249.930351451, -185341.62807085045 5371269.280603303)'), 
    loads('LINESTRING (-185295.81219471473 5371248.1178331785, -185288.3060748493 5371251.462322077, -185287.4998206596 5371251.7862683935, -185267.85933286787 5371259.302100101, -185259.55504311871 5371263.1080795)'), 
    loads('LINESTRING (-185298.89647704054 5371260.773153941, -185295.81219471473 5371248.1178331785)'), 
    loads('LINESTRING (-185215.8209704927 5371193.229017832, -185223.6284288762 5371199.668002385, -185232.1198364186 5371201.372823955)'), 
    loads('LINESTRING (-185232.1198364186 5371201.372823955, -185237.6839877006 5371202.423080438, -185246.69128494666 5371203.545087896)'), 
    loads('LINESTRING (-185172.28795219414 5371252.825501085, -185169.8899518544 5371242.476230796, -185166.51337440693 5371222.521779539, -185164.243655223 5371209.680098655)'), 
    loads('LINESTRING (-185358.42784761445 5371304.58992818, -185382.33982812922 5371290.193999024)'), 
    loads('LINESTRING (-185316.9262595013 5371335.629305901, -185335.298476488 5371320.595935468)'), 
    loads('LINESTRING (-185335.298476488 5371320.595935468, -185337.13650551558 5371319.106354396, -185356.29945160757 5371305.820651703, -185358.42784761445 5371304.58992818)'), 
    loads('LINESTRING (-185292.0559732729 5371354.775646643, -185314.04023351724 5371338.009378704, -185316.9262595013 5371335.629305901)'), 
    loads('LINESTRING (-185210.92892606626 5371385.681536197, -185243.3506096068 5371377.959434902, -185258.6623039958 5371374.013654168)'), 
]

points_gdf = gpd.GeoDataFrame(geometry=points)
network_gdf = gpd.GeoDataFrame(geometry=network)
partitioned, faces = c4.partition_networks(points_gdf, network_gdf)

fig = plt.figure(1, (12, 8))

sub1 = fig.add_subplot(111)
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

for n in network:
    path = Path(numpy.asarray(n.coords)[:, :2])
    sub1.add_patch(PathPatch(path, facecolor="none", edgecolor='gray', linewidth=1))

cmap = colormaps['Accent']
colors = cmap(numpy.linspace(0, 1, len(partitioned)))

for i, color in enumerate(colors):
    for p in partitioned[i]:
        coords = points[p].coords[0]
        sub1.plot(coords[0], coords[1], linestyle="", marker='o', color=color, markersize=5)

sub1.autoscale_view()
plt.show()