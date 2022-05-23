# face_verification

## face_verification API

### Idea
Use 2 apis, with:
- API for get embeedding
- API for calculate distance between 2 or more embbedding

Face verification in parking lot:
- Moto in:
    - Get embedding
    - Save embedding
    - Assume that save 10 faces (or more)

- Moto out:
    - Get embedding
    - Calculate distance with emb (1 out vs. 10 in)
    - Check with threshold
    - Continue until pass the threshold

### Timing
- OpenCV model
    - Get embeeding: 0.05525665283203125 s/image
    - Calculate distance: ~0.01 (10 embs in and 1 emb out)

    - Moto in: 10 images -> ~0.5s 
    - Moto out: 1 image + calc distance = 0.05 + 0.01 = 0.06. Assume that 10 out images -> 0.6s

### Run on Python
#### Get embbeding API
Run on http://localhost:8100
```
cd api
python app_get_emb.py
```

#### Get calculate distance API
Run on http://localhost:8200
```
cd api
python app_calc_distance.py
```

### API for C#
#### Get embbeding API

```
var client = new RestClient("http://0.0.0.0:8100/get_emb/");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AlwaysMultipartFormData = true;
request.AddParameter("image_path", "path_of_image (required lankmark information in filename)");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

Result
```
{
    "code": 200,
    "emb": "-0.18160109221935272, -0.1082758978009224, 0.012550609186291695, 0.006318273488432169, -0.013866093941032887, -0.03119257651269436, 0.07625716179609299, 0.01857079192996025, -0.007614081725478172, -0.17201828956604004, -0.026262035593390465, 0.18472246825695038, 0.021359233185648918, 0.022925954312086105, 0.2670423090457916, 0.0029997597448527813, -0.03974730148911476, -0.017982281744480133, -0.1888342797756195, 0.09469599276781082, -0.02734028920531273, -0.021598439663648605, -0.007767252158373594, -0.16791008412837982, -0.04786563664674759, 0.004684437997639179, 0.042749229818582535, -0.03504054993391037, 0.07828791439533234, -0.09698937088251114, 0.10053259879350662, -0.06831241399049759, 0.052968550473451614, 0.09620967507362366, -0.08333402127027512, 0.007894866168498993, -0.11045791208744049, -0.006064073648303747, -0.14710532128810883, -0.008694938383996487, 0.032305724918842316, 0.06374692916870117, -0.15836308896541595, -0.008062976412475109, -0.06952639669179916, -0.07843576371669769, -0.04988904669880867, -0.024558458477258682, 0.17688268423080444, -0.14447620511054993, -0.12807540595531464, -0.0698675736784935, -0.0747469887137413, 0.06840578466653824, 0.0945005863904953, 0.06222326681017876, -0.11755974590778351, -0.0356706902384758, 0.06685073673725128, -0.10058549791574478, -0.056348659098148346, 0.03810349479317665, -0.0405878983438015, -0.03347565233707428, -0.11700122058391571, -0.10513829439878464, 0.022854473441839218, 0.03316107019782066, -0.07607943564653397, -0.0200300682336092, -0.00031542929355055094, -0.028162289410829544, 0.022376568987965584, 0.015949029475450516, -0.1636357307434082, -0.17090143263339996, 0.12309927493333817, -0.06257543712854385, -0.1425917148590088, -0.0009570607217028737, 0.028099603950977325, -0.01751185767352581, 0.11364419013261795, 0.12438621371984482, -0.09742248803377151, 0.19378671050071716, -0.05159616097807884, -0.03817767649888992, -0.01736018806695938, 0.044490937143564224, -0.04152602329850197, 0.14748187363147736, 0.06509744375944138, 0.03730976581573486, 0.01833956688642502, 0.1708071380853653, 0.03619919344782829, -0.05694718286395073, 0.006328824907541275, 0.00040215838816948235, 0.07047245651483536, 0.08139052987098694, -0.004252476152032614, -0.038410644978284836, -0.0017205496551468968, 0.0056034354493021965, -0.04486604779958725, -0.00997250247746706, -0.11253613233566284, -0.05120806396007538, 0.18495003879070282, -0.010851548053324223, -0.01911475881934166, -0.03098950907588005, -0.004332957789301872, -0.008141989819705486, 0.05112465098500252, 0.05621232092380524, 0.1252182424068451, 0.009270680136978626, 0.10393233597278595, 0.07949204742908478, -0.15596206486225128, 0.12141237407922745, -0.10617899894714355, 0.06991966813802719, -0.1806355118751526, -0.00016208346642088145",
    "model": "opencv",
    "encode_type": "string"
}
```

Error
```
{
    "code": 201,
    "error_code": 0,
    "msg": "Message error"
}
```

#### Get calculate distance API

```
var client = new RestClient("http://0.0.0.0:8200/distance/");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AlwaysMultipartFormData = true;
request.AddParameter("in_emb_list", "-0.050550222396850586, -0.029276877641677856, 0.10202418267726898, -0.03997302055358887, -0.0798083022236824, 0.0514351986348629, 0.09584140032529831, -0.05747116729617119, -0.11737249791622162, -0.05591905117034912, 0.1298600435256958, 0.027082204818725586, 0.059563297778367996, 0.06148295849561691, 0.05388113483786583, -0.04777377471327782, -0.13259030878543854, -0.06190769001841545, -0.12166616320610046, 0.13470223546028137, -0.06847283989191055, -0.016603022813796997, -0.0040133302100002766, -0.04315997660160065, 0.05654254928231239, 0.10529126971960068, 0.05528029426932335, 0.13477538526058197, 0.04950650408864021, 0.17234112322330475, -0.06517006456851959, -0.08119931817054749, 0.07841867953538895, 0.14120452105998993, -0.04861437529325485, 0.04511924833059311, -0.08603569865226746, -0.13724489510059357, 0.060557447373867035, -0.06886551529169083, -0.05064669996500015, 0.12755508720874786, 0.10469792038202286, 0.09630008041858673, -0.013923981226980686, -0.1895628422498703, -0.10307416319847107, 0.016528351232409477, 0.057969868183135986, 0.001700055436231196, 0.041011545807123184, 0.05436054989695549, -0.047685407102108, 0.1295655220746994, 0.010212104767560959, -0.040579043328762054, 0.015456528402864933, -0.1684117615222931, 0.045632217079401016, -0.05171002075076103, -0.03131160885095596, 0.017200740054249763, -0.10618668794631958, 0.009789230301976204, -0.03593349829316139, -0.15940885245800018, 0.08779431134462357, 0.08306071907281876, 0.010410348884761333, 0.048784077167510986, -0.30760717391967773, 0.12495403736829758, 0.18156763911247253, -0.0006759726093150675, -0.06097378954291344, -0.16475750505924225, 0.07446888089179993, 0.0719275176525116, 0.022969359531998634, -0.09500090032815933, -0.08954045921564102, 0.034800779074430466, -0.027973635122179985, 0.06742292642593384, 0.10600274056196213, 0.012698391452431679, 0.11982596665620804, 0.07845768332481384, 0.0728263109922409, 0.1348617672920227, -0.07927463948726654, 0.10398631542921066, -0.03998782858252525, 0.08261321485042572, -0.03754331171512604, -0.030089888721704483, 0.01397890318185091, -0.06741920858621597, -0.009321046993136406, 0.10138881206512451, 0.06922461092472076, 0.04831164702773094, -0.1212158277630806, 0.03776772320270538, -0.053035225719213486, 0.07387619465589523, -0.0813128650188446, -0.05398127809166908, 0.02420315332710743, 0.0015909287612885237, 0.05158410593867302, -0.2254047989845276, -0.198506698012352, 0.050288718193769455, -0.09520905464887619, 0.050045523792505264, 0.035765547305345535, -0.0022952856961637735, 0.05393974483013153, -0.05307121202349663, 0.08178117871284485, -0.0001813380076782778, -0.08372733741998672, -0.11855846643447876, 0.005115720443427563, 0.10374689847230911, -0.06578508764505386, 0.028131874278187752
");
request.AddParameter("in_emb_list", "-0.10093697160482407, -0.0540112666785717, 0.09127315133810043, -0.06797004491090775, -0.09514082968235016, 0.030685868114233017, 0.11483319848775864, 0.005906043574213982, -0.1290227770805359, -0.1134488433599472, 0.14048151671886444, -0.012998350895941257, 0.08010337501764297, 0.0803808867931366, 0.0686328187584877, 0.021649541333317757, -0.15705198049545288, -0.07081925868988037, -0.11914501339197159, 0.08734647929668427, 0.004279048647731543, -0.07293680310249329, 0.0022265086881816387, -0.11269611865282059, 0.010154756717383862, 0.14236843585968018, 0.029846183955669403, 0.10589801520109177, 0.07413596659898758, 0.12531907856464386, -0.03663632646203041, -0.11541230231523514, 0.11025530099868774, 0.1676025092601776, -0.019595159217715263, -0.030610105022788048, -0.12962397933006287, -0.050094738602638245, -0.021076953038573265, -0.0953403115272522, -0.06527876853942871, 0.13829483091831207, 0.12331867963075638, 0.08331780135631561, -0.019229860976338387, -0.1360226422548294, -0.15048891305923462, 0.06700629740953445, 0.1389016956090927, -0.019062219187617302, -0.0754735916852951, 0.07814538478851318, 0.04684920608997345, 0.13534066081047058, 0.0047612315975129604, -0.0978507250547409, 0.01893019862473011, -0.19637362658977509, 0.014515741728246212, -0.051837529987096786, -0.07320191711187363, 0.028256388381123543, -0.11833665519952774, -0.0156369898468256, -0.05320148542523384, -0.15665943920612335, 0.05804036557674408, 0.04577834531664848, 0.03271793946623802, 0.05173414573073387, -0.21072690188884735, 0.1696060597896576, 0.1740361601114273, -0.01238680724054575, -0.04238628223538399, -0.17393800616264343, 0.127857506275177, 0.09052779525518417, 0.04093985632061958, -0.01366475597023964, -0.05365627631545067, -0.04532410576939583, 0.014765606261789799, 0.009440028108656406, 0.060011107474565506, -0.024937154725193977, 0.09871311485767365, 0.06233006343245506, 0.018144777044653893, 0.12214343994855881, -0.04854746162891388, 0.041089147329330444, 0.007294518873095512, -0.00040161513607017696, -0.017604678869247437, 0.050322525203228, 0.012592609040439129, -0.13826577365398407, 0.003655996872112155, 0.1471388190984726, 0.11367332935333252, 0.09162092208862305, -0.08488766849040985, -0.0006269066943787038, -0.12312065809965134, 0.06793764233589172, -0.0918864905834198, -0.04150824248790741, 0.014441676437854767, -0.0014776953030377626, 0.03936537355184555, -0.21485964953899384, -0.07329834997653961, 0.04336937889456749, -0.06880810856819153, 0.09456153213977814, 0.04156884551048279, -0.006837170105427504, 0.07284319400787354, -0.11567073315382004, -0.04322739690542221, 0.01808524876832962, -0.11535093933343887, -0.016666218638420105, 0.011129549704492092, 0.09165633469820023, -0.048713505268096924, 0.01668843999505043");
request.AddParameter("in_emb_list", "-0.18160109221935272, -0.1082758978009224, 0.012550609186291695, 0.006318273488432169, -0.013866093941032887, -0.03119257651269436, 0.07625716179609299, 0.01857079192996025, -0.007614081725478172, -0.17201828956604004, -0.026262035593390465, 0.18472246825695038, 0.021359233185648918, 0.022925954312086105, 0.2670423090457916, 0.0029997597448527813, -0.03974730148911476, -0.017982281744480133, -0.1888342797756195, 0.09469599276781082, -0.02734028920531273, -0.021598439663648605, -0.007767252158373594, -0.16791008412837982, -0.04786563664674759, 0.004684437997639179, 0.042749229818582535, -0.03504054993391037, 0.07828791439533234, -0.09698937088251114, 0.10053259879350662, -0.06831241399049759, 0.052968550473451614, 0.09620967507362366, -0.08333402127027512, 0.007894866168498993, -0.11045791208744049, -0.006064073648303747, -0.14710532128810883, -0.008694938383996487, 0.032305724918842316, 0.06374692916870117, -0.15836308896541595, -0.008062976412475109, -0.06952639669179916, -0.07843576371669769, -0.04988904669880867, -0.024558458477258682, 0.17688268423080444, -0.14447620511054993, -0.12807540595531464, -0.0698675736784935, -0.0747469887137413, 0.06840578466653824, 0.0945005863904953, 0.06222326681017876, -0.11755974590778351, -0.0356706902384758, 0.06685073673725128, -0.10058549791574478, -0.056348659098148346, 0.03810349479317665, -0.0405878983438015, -0.03347565233707428, -0.11700122058391571, -0.10513829439878464, 0.022854473441839218, 0.03316107019782066, -0.07607943564653397, -0.0200300682336092, -0.00031542929355055094, -0.028162289410829544, 0.022376568987965584, 0.015949029475450516, -0.1636357307434082, -0.17090143263339996, 0.12309927493333817, -0.06257543712854385, -0.1425917148590088, -0.0009570607217028737, 0.028099603950977325, -0.01751185767352581, 0.11364419013261795, 0.12438621371984482, -0.09742248803377151, 0.19378671050071716, -0.05159616097807884, -0.03817767649888992, -0.01736018806695938, 0.044490937143564224, -0.04152602329850197, 0.14748187363147736, 0.06509744375944138, 0.03730976581573486, 0.01833956688642502, 0.1708071380853653, 0.03619919344782829, -0.05694718286395073, 0.006328824907541275, 0.00040215838816948235, 0.07047245651483536, 0.08139052987098694, -0.004252476152032614, -0.038410644978284836, -0.0017205496551468968, 0.0056034354493021965, -0.04486604779958725, -0.00997250247746706, -0.11253613233566284, -0.05120806396007538, 0.18495003879070282, -0.010851548053324223, -0.01911475881934166, -0.03098950907588005, -0.004332957789301872, -0.008141989819705486, 0.05112465098500252, 0.05621232092380524, 0.1252182424068451, 0.009270680136978626, 0.10393233597278595, 0.07949204742908478, -0.15596206486225128, 0.12141237407922745, -0.10617899894714355, 0.06991966813802719, -0.1806355118751526, -0.00016208346642088145");
request.AddParameter("out_emb_list", "-0.16830022633075714, -0.09828994423151016, 0.057804182171821594, -0.019748596474528313, 0.10078945010900497, -0.11773853749036789, 0.023241743445396423, 0.0417017824947834, -0.06475158780813217, -0.008536813780665398, 0.04546257108449936, 0.11444200575351715, 0.04492447152733803, -0.07287383824586868, 0.002115266863256693, 0.018269585445523262, -0.03869614750146866, 0.026674123480916023, 0.04129646718502045, -0.011644805781543255, 0.1241123229265213, -0.06512373685836792, -0.055922046303749084, -0.08762934058904648, 0.0694018229842186, 0.09772773832082748, 0.0973747968673706, -0.06480564177036285, -0.02415855973958969, 0.043260954320430756, 0.09048508107662201, -0.009965983219444752, 0.020557882264256477, 0.15751506388187408, 0.06766651570796967, 0.0667596384882927, -0.04670223966240883, 0.22731530666351318, -0.050235893577337265, 0.05436114966869354, 0.14709264039993286, -0.026780646294355392, -0.09553351253271103, -0.01327110081911087, 0.0025577214546501637, -0.06682586669921875, -0.03957453370094299, -0.1602557748556137, -0.036036670207977295, 0.08203452825546265, 0.0769423395395279, -0.025467602536082268, -0.0519222654402256, 0.12944698333740234, -0.017901413142681122, 0.08170028775930405, 0.11825618892908096, -0.11818288266658783, -0.04515206068754196, -0.010877441614866257, 0.005512382369488478, 0.03132655844092369, -0.06708645075559616, -0.10815978795289993, -0.069771409034729, -0.0682682991027832, -0.09002309292554855, -0.08601290732622147, -0.19253580272197723, 0.04825184866786003, 0.19793923199176788, 0.13311997056007385, 0.008239082992076874, 0.027798941358923912, 0.10541949421167374, -0.09770122170448303, 0.053353872150182724, -0.03569887578487396, -0.01820693165063858, -0.1917334794998169, 0.0057074688374996185, -0.056344978511333466, -0.05336248502135277, 0.11561248451471329, 0.05999438464641571, -0.07820174098014832, -0.011829917319118977, -0.1604272723197937, 0.17470090091228485, 0.03260832652449608, -0.2461756318807602, -0.013948398642241955, -0.01449450571089983, 0.007752866484224796, 0.06403830647468567, 0.21035632491111755, 0.07379915565252304, -0.12361206859350204, -0.11009155958890915, 0.09639669954776764, 0.04199066013097763, 0.07471150159835815, 0.15287253260612488, -0.029745882377028465, 0.04586320370435715, 0.05022469907999039, -0.04284988343715668, 0.04582292214035988, 0.024414772167801857, -0.01696399413049221, 0.07644542306661606, -0.02544294111430645, -0.020283276215195656, -0.08655108511447906, 0.10766978561878204, 0.017291029915213585, -0.028993304818868637, -0.012557191774249077, 0.10627181828022003, 0.07984787225723267, -0.09526253491640091, 0.0389358289539814, -0.06766045838594437, 0.04134874418377876, 0.2318885773420334, -0.08169036358594894, -0.007260534446686506, -0.026059161871671677");
request.AddParameter("out_emb_list", "-0.16830022633075714, -0.09828994423151016, 0.057804182171821594, -0.019748596474528313, 0.10078945010900497, -0.11773853749036789, 0.023241743445396423, 0.0417017824947834, -0.06475158780813217, -0.008536813780665398, 0.04546257108449936, 0.11444200575351715, 0.04492447152733803, -0.07287383824586868, 0.002115266863256693, 0.018269585445523262, -0.03869614750146866, 0.026674123480916023, 0.04129646718502045, -0.011644805781543255, 0.1241123229265213, -0.06512373685836792, -0.055922046303749084, -0.08762934058904648, 0.0694018229842186, 0.09772773832082748, 0.0973747968673706, -0.06480564177036285, -0.02415855973958969, 0.043260954320430756, 0.09048508107662201, -0.009965983219444752, 0.020557882264256477, 0.15751506388187408, 0.06766651570796967, 0.0667596384882927, -0.04670223966240883, 0.22731530666351318, -0.050235893577337265, 0.05436114966869354, 0.14709264039993286, -0.026780646294355392, -0.09553351253271103, -0.01327110081911087, 0.0025577214546501637, -0.06682586669921875, -0.03957453370094299, -0.1602557748556137, -0.036036670207977295, 0.08203452825546265, 0.0769423395395279, -0.025467602536082268, -0.0519222654402256, 0.12944698333740234, -0.017901413142681122, 0.08170028775930405, 0.11825618892908096, -0.11818288266658783, -0.04515206068754196, -0.010877441614866257, 0.005512382369488478, 0.03132655844092369, -0.06708645075559616, -0.10815978795289993, -0.069771409034729, -0.0682682991027832, -0.09002309292554855, -0.08601290732622147, -0.19253580272197723, 0.04825184866786003, 0.19793923199176788, 0.13311997056007385, 0.008239082992076874, 0.027798941358923912, 0.10541949421167374, -0.09770122170448303, 0.053353872150182724, -0.03569887578487396, -0.01820693165063858, -0.1917334794998169, 0.0057074688374996185, -0.056344978511333466, -0.05336248502135277, 0.11561248451471329, 0.05999438464641571, -0.07820174098014832, -0.011829917319118977, -0.1604272723197937, 0.17470090091228485, 0.03260832652449608, -0.2461756318807602, -0.013948398642241955, -0.01449450571089983, 0.007752866484224796, 0.06403830647468567, 0.21035632491111755, 0.07379915565252304, -0.12361206859350204, -0.11009155958890915, 0.09639669954776764, 0.04199066013097763, 0.07471150159835815, 0.15287253260612488, -0.029745882377028465, 0.04586320370435715, 0.05022469907999039, -0.04284988343715668, 0.04582292214035988, 0.024414772167801857, -0.01696399413049221, 0.07644542306661606, -0.02544294111430645, -0.020283276215195656, -0.08655108511447906, 0.10766978561878204, 0.017291029915213585, -0.028993304818868637, -0.012557191774249077, 0.10627181828022003, 0.07984787225723267, -0.09526253491640091, 0.0389358289539814, -0.06766045838594437, 0.04134874418377876, 0.2318885773420334, -0.08169036358594894, -0.007260534446686506, -0.026059161871671677");
request.AddParameter("out_emb_list", "-0.13866138458251953, -0.10385283827781677, -0.03999613970518112, 0.047888681292533875, 0.11713758111000061, -0.08775307983160019, 0.1044282540678978, 0.10050062835216522, -0.13214142620563507, -0.08820483833551407, 0.035685040056705475, 0.231365367770195, 0.040585242211818695, 0.05611323192715645, 0.23430633544921875, -0.059333302080631256, -0.06782216578722, -0.09637277573347092, -0.15755115449428558, 0.02880101650953293, 0.005240316968411207, 0.11368222534656525, -0.004561778157949448, -0.10063818842172623, -0.12008915096521378, 0.06352834403514862, 0.06323288381099701, -0.027899499982595444, 0.0016261226264759898, -0.016270795837044716, 0.037385355681180954, -0.013226481154561043, 0.0019970573484897614, 0.09638405591249466, -0.014391040429472923, 0.07762140780687332, -0.0900987908244133, 0.11534316837787628, -0.1680755615234375, -0.09753723442554474, 0.05167481303215027, -0.07373341172933578, -0.06403243541717529, 0.019398711621761322, 0.00351314852014184, -0.090410515666008, -0.044974010437726974, -0.07604069262742996, -0.018125295639038086, -0.042473550885915756, -0.05358078330755234, 0.01131570152938366, -0.10804421454668045, 0.17565575242042542, 0.0654396042227745, 0.17574161291122437, -0.0792141854763031, -0.17519862949848175, -0.09701613336801529, -0.10315824300050735, 0.03676260635256767, -0.031296443194150925, 0.04500238969922066, 0.10225863754749298, -0.06597290933132172, -0.04122235253453255, 0.04314813017845154, 0.07656461745500565, -0.08871966600418091, 0.1016719788312912, 0.02189343050122261, 0.08046161383390427, 0.10669174790382385, -0.025333527475595474, -0.1233685165643692, -0.07584726810455322, 0.00019977788906544447, 0.02304481528699398, -0.027114899829030037, 0.03591145947575569, -0.10391020029783249, -0.04297005012631416, -0.006389039568603039, 0.08837448060512543, 0.01293268520385027, 0.10270464420318604, -0.005227635148912668, 0.020887907594442368, 0.1175433024764061, 0.16707690060138702, -0.0920277088880539, 0.10234875977039337, 0.14948499202728271, 0.003063941141590476, 0.08815474808216095, 0.04294952377676964, -0.0698135495185852, -0.06573998928070068, -0.012377220205962658, 0.17062291502952576, 0.10398160666227341, 0.09197231382131577, -0.09871576726436615, -0.07916077971458435, -0.006696768570691347, -0.07292110472917557, -0.06270201504230499, 0.09830696880817413, -0.00920469593256712, 0.043917570263147354, 0.03928855434060097, -0.04030337557196617, -0.18763768672943115, -0.05571203678846359, 0.025201698765158653, -0.010695465840399265, 0.048047542572021484, -0.050074782222509384, 0.08431635051965714, 0.1786036491394043, 0.033751823008060455, 0.09720155596733093, -0.06476106494665146, 0.07590601593255997, 0.011469636112451553, -0.08858850598335266, -0.03608843311667442, -0.15918314456939697");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

Result
```
{
    "code": 200,
    "distance": "0.9410259223306792",
    "measure": "euclidean",
    "model": "opencv",
    "encode_type": "string"
}
```

Error
```
{
    "code": 201,
    "error_code": 0,
    "msg": "operands could not be broadcast together with shapes (3,) (3,1,128) "
}
```