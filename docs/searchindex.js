Search.setIndex({docnames:["Basic pipeline","Events and statistics from ROIs","Image transformations","Integration with databases","Object detection","Object tracking","background","database","devnotes","examples","index","intro","object_detection","object_tracking","pipeline","references","requirements","roi","sinks","sources","utils","zeromq"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,"sphinx.ext.todo":2,nbsphinx:3,sphinx:56},filenames:["Basic pipeline.nblink","Events and statistics from ROIs.nblink","Image transformations.nblink","Integration with databases.nblink","Object detection.nblink","Object tracking.nblink","background.rst","database.rst","devnotes.rst","examples.rst","index.rst","intro.rst","object_detection.rst","object_tracking.rst","pipeline.rst","references.rst","requirements.txt","roi.rst","sinks.rst","sources.rst","utils.rst","zeromq.rst"],objects:{"videoanalytics.pipeline":{Pipeline:[14,1,1,""],Sink:[14,1,1,""],Source:[14,1,1,""],sinks:[18,0,0,"-"],sources:[19,0,0,"-"]},"videoanalytics.pipeline.Pipeline":{execute:[14,2,1,""],get_metrics:[14,2,1,""],get_total_execution_time:[14,2,1,""],optimize:[14,2,1,""],plot:[14,2,1,""]},"videoanalytics.pipeline.Sink":{__init__:[14,2,1,""],enable_display:[14,2,1,""],process:[14,2,1,""],setup:[14,2,1,""],shutdown:[14,2,1,""],toggle_display_enable:[14,2,1,""]},"videoanalytics.pipeline.Source":{__init__:[14,2,1,""],get_progress:[14,2,1,""],read:[14,2,1,""],setup:[14,2,1,""],shutdown:[14,2,1,""]},"videoanalytics.pipeline.sinks":{ImageWriter:[18,1,1,""],VariableCSVWriter:[18,1,1,""],VideoWriter:[18,1,1,""],background:[6,0,0,"-"],database:[7,0,0,"-"],object_tracking:[13,0,0,"-"],zmq:[21,0,0,"-"]},"videoanalytics.pipeline.sinks.ImageWriter":{process:[18,2,1,""],setup:[18,2,1,""],shutdown:[18,2,1,""]},"videoanalytics.pipeline.sinks.VariableCSVWriter":{process:[18,2,1,""],setup:[18,2,1,""],shutdown:[18,2,1,""]},"videoanalytics.pipeline.sinks.VideoWriter":{process:[18,2,1,""],setup:[18,2,1,""],shutdown:[18,2,1,""]},"videoanalytics.pipeline.sinks.background":{BackgroundExtractor1:[6,1,1,""],BackgroundExtractor2:[6,1,1,""]},"videoanalytics.pipeline.sinks.background.BackgroundExtractor1":{process:[6,2,1,""],setup:[6,2,1,""],shutdown:[6,2,1,""]},"videoanalytics.pipeline.sinks.background.BackgroundExtractor2":{process:[6,2,1,""],setup:[6,2,1,""],shutdown:[6,2,1,""]},"videoanalytics.pipeline.sinks.object_tracking":{TrackedObjectsAnnotator:[13,1,1,""],TrackedObjectsCSVWriter:[13,1,1,""]},"videoanalytics.pipeline.sinks.object_tracking.TrackedObjectsAnnotator":{process:[13,2,1,""],setup:[13,2,1,""],shutdown:[13,2,1,""]},"videoanalytics.pipeline.sinks.object_tracking.TrackedObjectsCSVWriter":{process:[13,2,1,""],setup:[13,2,1,""],shutdown:[13,2,1,""]},"videoanalytics.pipeline.sinks.zmq":{ZMQPub:[21,1,1,""]},"videoanalytics.pipeline.sinks.zmq.ZMQPub":{process:[21,2,1,""],setup:[21,2,1,""],shutdown:[21,2,1,""]},"videoanalytics.pipeline.sources":{ImageSequenceReader:[19,1,1,""],VideoReader:[19,1,1,""]},"videoanalytics.pipeline.sources.ImageSequenceReader":{get_progress:[19,2,1,""],read:[19,2,1,""],setup:[19,2,1,""],shutdown:[19,2,1,""]},"videoanalytics.pipeline.sources.VideoReader":{get_progress:[19,2,1,""],read:[19,2,1,""],setup:[19,2,1,""],shutdown:[19,2,1,""]},"videoanalytics.utils":{read_class_names:[20,3,1,""]},videoanalytics:{pipeline:[14,0,0,"-"],utils:[20,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function"},terms:{"0":[0,1,2,3,4,5,9,16,17,19,21],"0000":4,"00000":4,"000000":4,"000008":1,"000013":3,"000018":5,"000040":4,"00008":4,"000296":1,"00032":4,"000330":5,"000456":5,"000493":4,"000503":1,"00064":4,"000865":5,"000981":2,"005932":1,"006297":0,"006368":4,"007867":5,"008531":1,"008902":2,"009327":5,"011074":3,"011527":2,"011698":3,"016689":1,"021735":4,"022153":0,"024441":5,"030035":1,"030239":5,"030823":5,"045736":3,"047086":4,"048645":3,"065422":4,"08":3,"087228":3,"08t00":3,"0963284800018":1,"0rc0":16,"1":[0,1,2,3,4,5,9,11,16,19,21],"10":[0,1,2,4,5,9,16],"100":[0,2,3,4,5],"1000":[1,4],"10000":1,"10001":1,"10002":1,"10003":1,"10004":1,"1018":4,"102":5,"104":[4,5],"1042":4,"1057":[1,17],"1059":4,"1067":4,"1068":[1,17],"107":1,"1072":[1,17],"1073":[1,17],"1074":[1,17],"108":5,"1080":4,"1088":[1,17],"109":1,"11":[0,1,2,4,5,16,17],"110":4,"111":[4,5],"1118":4,"1125":4,"1131":[1,17],"1134":4,"118":1,"1191":4,"12":[0,1,2,4,5,16],"120":4,"1202":4,"1209":4,"1210":[1,17],"125":1,"126":1,"127":[4,21],"1281":4,"1287":4,"13":[0,1,3,4,5],"130":4,"132491":3,"134":4,"135":1,"136":1,"137":[1,4,5],"14":[0,1,3,4,5,16],"140":[3,4,5],"1430":4,"1456":4,"15":[0,3,4,5,16],"150":[1,4],"1500":4,"1522":[1,17],"153":1,"155":[1,17],"156":1,"1565":[1,17],"16":[1,3,4,5,16],"165":[1,17],"1651":4,"17":[1,3,4,5,16],"171607":3,"1749":[1,17],"175875368004199":2,"18":[1,3,4,5,16],"1801":4,"1827":4,"185":4,"18773640099971":[],"19":[3,4,5],"1904":[1,17],"1920":4,"2":[0,1,2,3,4,5,9,14,16],"20":[1,4,5,16],"2021":[3,16],"21":[1,4],"216":4,"22":[0,1,2,3,4,5],"23":[1,4],"233":1,"236":1,"24":[1,3,4],"240":2,"25":[1,3,4,16],"253":4,"254455":4,"255":[1,17],"256k":4,"26":[1,4,16],"2606":4,"27":[1,4],"271":1,"28":[1,3,4,16],"280":4,"29":[1,4,16],"2fp":4,"3":[0,1,2,3,4,5,9,14,16],"30":[1,3,4,16],"301":4,"305":[1,4,17],"31":4,"311861097000474":4,"315":[1,17],"32":4,"320":2,"329":4,"32k":4,"33":4,"333":4,"334":[1,17],"336":[1,17],"338":4,"34":[1,4],"341":4,"35":4,"3500":4,"352":4,"35206350700173":5,"358":1,"36":[3,4],"361":[4,5],"362":4,"363828":3,"365":4,"369":[1,17],"37":[3,4,16],"38":[3,4],"382":[1,17],"385":[1,17],"387":[4,5],"388":4,"39":[3,4],"3dnowprefetch":4,"4":[0,1,2,3,4,5,9,16,17],"40":[1,3,4],"400":[0,1,2,3,4,5],"41":[3,4],"416":[1,3,4,5],"42":3,"426":4,"45":3,"456":4,"460":4,"468":4,"47":3,"479":1,"48":3,"481":4,"482754":4,"483":4,"49":3,"491":4,"494261":4,"498":4,"499":4,"49952":4,"49960":4,"5":[0,1,2,3,4,5,9,15,16,17],"50":3,"5000":21,"51":4,"51667647999966":4,"518353":3,"519":4,"5199":4,"525":4,"525466":3,"5262541174888611":3,"532":[1,17],"537":4,"538":[1,17],"54":1,"541":4,"542":4,"545455":4,"556":4,"559":4,"559688":5,"56":1,"5600":21,"568":4,"57":1,"570":[1,17],"575191":3,"58":1,"580":[1,17],"583":4,"584":[1,17],"589164":4,"59":1,"592":[1,17],"595":[1,17],"6":[0,1,2,3,4,5,9,16],"60":[5,16],"600":[0,1,2,3,4,5],"606":[1,17],"60ghz":4,"61":1,"612":4,"6144k":4,"61873008300608":3,"61876826400112":1,"620463":3,"6205215454101562":3,"620522":4,"625":[1,4,17],"629002":4,"63":1,"633901059627533":3,"6384348273277283":3,"6390221118927002":3,"64":4,"641":4,"646":4,"648":1,"65":1,"655":1,"6578598618507385":3,"657860":4,"66":3,"666":[1,17],"667":4,"668":[1,17],"67":1,"6700hq":4,"672495":4,"676":[1,17],"682":[1,17],"692927":5,"696":[4,5],"7":[0,1,2,3,4,5,16],"703006":1,"706":4,"708":1,"718696":4,"719":1,"72":[],"735088":3,"737":4,"742915":4,"7429153323173523":3,"7459518609976":1,"75":5,"753":4,"754":[1,17],"757":[1,17],"766":4,"767":1,"771":4,"773":[1,17],"777":[1,17],"795":1,"796":1,"8":[0,1,2,3,4,5,16],"800":4,"8000":3,"8001":3,"8002":3,"8003":3,"8004":3,"804":4,"807":4,"8086":3,"810":[1,17],"827":1,"83832986899506":5,"856067":3,"860":[4,5],"862":4,"862434":4,"886986176999926":0,"896999":4,"9":[0,1,2,4,5,16],"90":4,"908":[1,17],"931":4,"94":4,"949":[1,17],"954":[1,17],"973":[1,17],"98":4,"999":4,"99904":4,"99936":4,"99948":4,"99950":4,"99958":4,"99960":4,"99962":4,"99968":4,"99970":4,"99972":4,"99974":4,"99976":4,"99980":4,"99984":4,"99994":4,"99996":4,"abstract":[14,18,19],"byte":4,"case":[3,4,10,14],"catch":1,"class":[1,3,4,5,6,13,14,18,19,20,21],"default":[4,14,18,19],"export":8,"final":[4,14],"float":[],"function":[4,20],"import":[0,1,2,3,4,5,9],"int":19,"new":[1,18],"public":11,"return":[4,14,19,20],"true":[1,3,4],"try":11,"while":14,A:[3,10,20],As:[11,17],But:11,By:4,For:[0,4,11],If:[1,17],In:[3,4],Is:1,It:[11,18],On:4,The:[0,1,4,10,11,12,13,15,17,18,19],Their:14,These:14,To:[4,5],__init__:14,__main__:9,__name__:9,_count:3,_sourc:3,abl:11,abm:4,absolut:[],academ:11,accept:[],access:14,achiev:18,acitv:1,acpi:4,acquir:14,acquisit:19,action:[14,18],activ:[6,11,13,14,17,18,21],acycl:14,ad:[],adapt:20,add:[0,1,2,3,4,5,9],add_compon:[0,1,2,3,4,5,9],addit:14,adjust:[],adopt:[],advanc:3,adx:4,ae:4,affect:2,aforement:14,after:[0,6,13,14,18,19,21],ag:[],alabast:16,alarm:[1,11],algorithm:[4,10,11,13,14],align:[0,1,2,3,4,5],all:[4,6,13,14,18,19,21],allow:3,allowed_class:[],alpha:1,also:[3,4,12,14],altern:12,alwai:19,amount:17,an:[0,1,2,4,11,12,13,14,17,19,20],analysi:[4,11,15],analyt:[10,15],analyz:11,anayisi:5,ani:[2,12,18],annot:[1,3,4,5,12,13,15],annotator_avg_dt:4,anot:14,anoth:14,aperfmperf:4,api:10,apic:4,appdir:16,append:4,applehelp:16,appli:[14,17],applic:[1,3,14],approach:[1,11,18],ar:[0,2,3,4,5,6,10,11,12,13,14,17,18,19,21],arat:4,arch_perfmon:4,architectur:[4,11],area:[1,17],around:13,arrai:[13,14,18,19],arrow:14,art:4,articl:15,aspect:14,assign:[],assist:4,associ:[1,15,17],associate_detections_to_track:[],assum:14,assumpt:1,astunpars:16,async:16,attribut:[2,19],audio:19,auth:16,automat:[11,14],autoreload:[0,1,2,3,4,5],avail:[2,11,14],averag:[4,14,15,16],avg_exec_tim:4,avi:[0,1,2,3,4,5],avx2:4,avx:4,ax:[0,1,2,3,4,5,14],b:0,babel:16,background:[10,14],backgroundextractor1:6,backgroundextractor2:6,bar:1,base:[11,14],basic:[2,4,5,10],becaus:11,been:15,befor:11,behind:11,being:[1,4,17,19],below:[],best:14,between:[4,14],bibliographi:15,bit:4,blackboard:14,block:[10,11,14],bmi1:4,bmi2:4,board:17,bodi:3,bogomip:4,bool:[],both:[4,11],bottom:[],bound:[1,4,5,13],box:[1,4,5,13],box_format:4,bt:4,buffer:19,build:[4,9,10,14,16],built:18,cach:4,cachetool:16,call:[6,13,14,18,19,21],callback:14,camera:[1,11,14,17],can:[1,3,4,11,14,17,19],cancel:[14,19],capabl:11,captur:[1,19],car:11,cat:1,categori:[12,14],cell:[],center:[0,1,2,3,4,5],certain:1,certifi:16,cffi:16,chain:14,chang:[],chardet:16,checkpoint:[1,3,4,5],checkpoints_path:4,children:14,class_id:3,class_idx:[3,4],class_names_filenam:[1,4],classes_definit:[1,3,4,5],classes_to_count:3,classif:[14,17],classifi:1,clflush:4,clflushopt:4,client:3,cmd2:16,cmov:4,coco:[1,3,4,5],code:[11,15],codebas:11,collect:[4,11],color:[1,17],colorama:16,column:[0,1,2,3,4,5],com:21,combin:[11,17],commun:[10,14],compat:19,complex:[11,14,18],compon:[0,1,2,3,5,6,9,10,11,12,13,18,19,20,21],component:21,compos:14,compris:10,comput:[11,14,15],concept:[14,18,19],concern:[3,11],conda:8,confid:[],configur:[10,14,18],connect:[1,2,3,4,5,9,11],consid:[4,14],consisti:14,constant_tsc:4,construct:[],constructor:14,consult:15,consumpt:[12,14],contain:[3,4,9,13,14,15,18,19,20],contempl:19,content:[1,3,4,5,11,15],context:[0,1,2,3,4,5,6,9,13,14,18,19,21],contigu:4,control:[0,1,2,3,4,5,11],conveni:[4,14],convent:[],convers:20,convert:[4,15],convert_detect:4,coordin:[],cope:19,core:[4,14,19],correspond:[],cosin:15,could:[1,4,12,19],count:[3,11],counter:1,cpu:[4,14],cpuid:4,cpuid_fault:4,creat:[0,1,2,3,4,5,9,14],crowd:4,cryptographi:16,csv:[1,3,4,5,12,13,18],csv_variabl:1,current:[0,1,2,4,5,14,18,19],custom:11,cv3dst:15,cvat:15,cx16:4,cx8:4,cycler:16,d:3,darknet:[12,20],dash:14,data:[0,1,2,3,4,5,9,11,14,18,20],data_path:[0,1,2,3,4,5,9],databas:[10,18],datafram:[0,1,2,3,4,5],dataset:15,datfram:4,db:[3,11,14],de:4,decis:14,deck:[1,17],declar:14,decor:16,dedic:3,deep:[12,15],deeper:1,deepsort:[1,10,15],deepsort_model_filenam:[1,5],def:4,defin:[0,1,2,3,4,5,9,11,14],definin:0,definit:10,depend:[12,14],describ:[10,11,12],descript:[10,13,18,19],design:[3,10,14],desir:2,det:[],det_csv_writ:4,det_csv_writer_avg_dt:4,det_list:4,detail:[10,11,19],detcount:3,detcounter_avg_dt:3,detect:[1,3,5,10,11,14,15,16],detections_csv_filenam:4,detections_filenam:[1,3,4,5],detectionsannot:[1,3,4,5],detectionscount:3,detectionscsvwrit:[1,3,4,5],detectionseswrit:3,detector:[1,3,4,5,13,17],detector_avg_dt:[1,3,4,5],detector_classes_filenam:[1,3,4,5],detector_weights_filenam:[1,3,4,5],determin:11,detmetr:16,devhelp:16,devic:[14,19],df:1,df_gt_det:4,df_model_sel_result:4,df_od_metr:4,df_pipeline_metr:4,df_pred_det:4,df_track:5,dicitonari:[],dict:[13,14,18,19,20],dictionari:[4,14,20],didnt:4,differ:[4,9,14,17,19],difficult:4,dimens:[],direct:14,directli:15,directori:4,discuss:10,displai:[0,2,4,5,13,14],distlib:16,div:[0,1,2,3,4,5],divis:14,docker:21,document:[3,8],docutil:16,doe:14,domain:14,download:[0,1,2,3,4,5],drop:19,ds_cpl:4,dt:4,dtes64:4,dtherm:4,dtype:[],dure:[11,14],dynam:11,each:[0,1,3,4,5,6,11,13,14,17,18,19,20,21],easydict:16,ecosystem:11,edn:15,elasticsearch:10,elasticsearch_hostnam:3,elasticsearch_index:3,element:19,empti:[],enable_displai:14,end:14,endian:4,endpoint:21,enter:[1,11,17],entiti:11,entri:[13,18,19],entrypoint:16,env:8,environ:8,epb:4,ept:4,erm:4,es:3,es_index:3,est:4,estim:[10,11,14,17],eswrit:3,eswriter_avg_dt:3,etc:[1,17,18],eval_img_list:4,evalu:[10,14,15],evaluate_object_detection_predict:4,even:[4,11],event:[3,11,17],evolut:11,exampl:[0,1,2,3,4,5,11,12,14,17,18,20],execut:[0,2,3,5,9,10,11,14],exist:11,expect:4,experiment:11,explor:[10,11],express:0,extend:19,extern:11,extract:11,f16c:4,face:11,fals:4,famili:4,fast:[3,11],field:[],fig:[0,1,2,3,4,5,11,14,17],figsiz:[0,1,2,3,4,5],file:[0,4,13,14,18,19,20],filelock:16,filenam:[0,1,2,3,4,5,9,13,18,19,20],filterpi:16,finish:[6,13,14,18,19,21],fire:11,first:[2,10,12,19],fix:[1,17],fixm:[1,6,7,21],flag:4,fledg:11,flexprior:4,float64:[],flush_l1d:4,fma:4,focu:[3,11],follow:[0,1,4,11,13,15,18,19],follw:10,footag:[1,3,17],format:[0,1,2,3,4,5,10,12,18,20],fp:[2,18,19],fpu:4,fragment:[4,19],frame:[0,1,2,3,5,10,11,13,14,18,19,21],frame_num:[1,4,5],framer:19,framework:[11,12],freez:8,from:[0,2,3,4,5,6,9,11,12,13,14,15,17,18,19,21],from_dict:[0,1,2,3,4,5],frozen:4,fsgsbase:4,fulfil:[],fulli:11,furtherli:14,fxsr:4,gast:16,gener:[1,8,11,13,14,16,18],genuineintel:4,geometri:1,get:14,get_metr:[0,1,2,3,4,5,9,14],get_progress:[14,19],get_total_execution_tim:[0,1,2,3,4,5,14],given:4,glob:4,global:[0,1,2,3,4,5,13,14,18,19],googl:16,got:3,gpu:[8,16],grant:14,graph:[0,4,14],grid:[1,11],ground:4,group:14,groupbi:1,grpc:12,grpcio:16,guarante:19,guidelin:10,h5py:16,h:[4,5],ha:[0,1,4],happen:17,have:15,head:[1,4,5],heavili:14,height:[0,1,2,3,4,5,18,19],high:19,hit:3,hle:4,hold:[],host:[3,21],hostnam:3,how:[3,4,9,11,17],ht:4,html:[0,1,2,3,4,5],htmlhelp:16,http:21,hub:21,human:17,hwp:4,hwp_act_window:4,hwp_epp:4,hwp_notifi:4,i7:4,ibpb:4,ibr:4,id:[4,13,20],ida:4,idea:11,identif:[3,4],identifi:[5,11,13],idna:16,ii:15,illustr:[0,1,11],imag:[4,10,18,19,21],images:16,imagesequenceread:[4,18,19],imagewrit:[4,18],img10606:4,img10956:4,img10989:4,img11071:4,img12115:4,img12419:4,img15269:4,img1603:4,img16322:4,img16689:4,img2264:4,img2334:4,img365:4,img5320:4,img7463:4,img8240:4,img8243:4,img8722:4,img9859:4,img:4,img_filenam:[18,19],img_h:4,img_list:4,img_nam:4,img_path:4,img_seq:[4,19],img_w:4,implement:[4,10,11,14,15,19],improv:4,includ:[11,12,15],increment:[],independ:12,index:[0,1,2,3,4,5,10],index_mod:3,indic:[0,1,14],individu:[4,5],infer:[1,4],influxdb:10,influxdb_avg_dt:3,influxdb_hostnam:3,influxdb_password:3,influxdb_schema:3,influxdb_usernam:3,influxdbcli:3,influxdbwrit:3,inform:[11,13,14,15,17,19],inherit:14,iniconfig:16,initi:[2,11,14],inmut:2,input:[0,2,3,5,9,10,18,19],input_avg_dt:[0,1,2,3,4,5],input_fp:[18,19],input_height:[18,19],input_video:[0,1,2,3,4,5,9],input_width:[18,19],insert:3,insid:17,insight:[1,17],inspir:14,instanc:[1,3,6,13,14,18,19,21],instanti:[2,10],instead:4,integr:[10,11],intel:4,intel_pt:4,interact:18,interest:[1,3,4,17],interfac:[14,19],intern:[],interpret:4,introduc:3,introduct:[10,15],involv:11,invpcid:4,invpcid_singl:4,iou:[],iou_threshold:[],isol:[0,2,14],item:4,iter:[2,14,19],its:[10,12,13,14],itself:11,jedi:16,jeepnei:16,jpg:4,jsmath:16,json:[1,3,10],jupyt:[0,1,2,4,5,16],keep:[4,14],kei:[],kera:[11,16],kind:14,known:[14,19],l1d:4,l1i:4,l2:4,l3:4,lahf_lm:4,languag:3,last:[],later:4,learn:[11,12,15],leav:[11,17],lectur:15,left:1,legend:1,length:[14,19],let:11,librari:[2,9,10,11,12,14,15],limit:2,line:4,link:16,list:[3,4,11,18,19],littl:4,lm:4,load:12,load_detections_from_file_list:4,load_ext:[0,1,2,3,4,5],loc:4,localhost:[3,21],locat:11,lower:1,lower_left:1,lower_right:1,lscpu:4,made:11,mai:[],main:[],make:[4,8],make_pipelin:4,mantain:14,map:[4,15,20],mar:[1,5],mask:11,match:[4,18],match_al:3,matplotlib:[0,1,2,3,4,5,14,16],max:4,max_ag:[],max_fram:[0,1,2,3,4,5,9,19],maximum:19,mca:4,mce:4,md_clear:4,mean:[15,16],meaning:[11,19],meant:21,measur:14,memori:14,met:14,method:[3,4,6,10,13,14,18,19,21],metric:[4,14,15,16],metrics_df:[0,1,2,3,4,5],mhz:4,middlewar:14,might:[1,10,14],min:4,min_hit:[],minim:10,minimum:[],minor:[],mirtar:1,miscelan:20,mission:11,mmx:4,mode:4,model:[1,3,5,10,12,14,15],model_filenam:[1,5],model_nam:4,model_param:4,models_to_test:4,modifi:4,modul:[10,13,14,18,19,20],monitor:4,monolith:18,more:[1,4,10,11,14,20],most:[4,19],motion:[10,11,14,17],motiv:10,movb:4,movement:[6,17],mp4:[0,1,2,3,4,5,9],mpeg:21,mpx:4,msr:4,mtrr:4,multipl:2,must:2,my_appl:3,myst:16,n:1,n_:[],naiv:19,name:[1,3,4,5,8,13,14,17,18,19,20,21],nan:4,navig:11,nbsphinx:16,necesarili:14,need:[2,4,14],network:[1,21],networkx:16,nhorro:21,node0:4,node:4,none:[2,4,14,18,19],nonstop_tsc:4,nopl:4,normal:4,note:[0,1,2,3,4,5,14,18],notic:14,np:[],num_box:[],numa:4,number:[1,3,11,17,19],numer:13,numpi:[13,14,16,18,19],nx:4,oauthlib:16,obj_00_count:3,obj_:3,obj_id:[1,5],object:[3,10,11,14,15,16,17],object_detect:[1,3,4,5],object_track:[1,5,13],objectdetectorcsv:[],observ:11,obtain:[1,4,14,19],occupi:4,onc:[],one:[3,14,20],ones:11,onli:[0,4,14,19],onlin:[1,15],op:4,opencv:[11,12,16,18,19],openlabel:15,oper:[14,17],optim:[0,1,2,3,4,5,14],option:[0,1,2,3,4,5,9,19],order:[0,4,14],organ:[10,11,15],organis:10,orient:[0,1,2,3,4,5],origin:15,os:4,other:[4,11,12,14,15,17,19],out_box:[],out_class:[],out_scor:[],output:[0,2,3,5,9,10,11,13,14,18,19],output_format:18,output_h:2,output_img_path:4,output_path:[4,18],output_video:[0,1,2,3,4,5,9],output_w:2,overlap:[],pacakag:11,packag:[8,11],pae:4,page:10,panda:[0,1,2,3,4,5,16],paper:15,paradigm:[10,11],paramet:[3,4,13,18,19,20],parent:[],parser:16,part:[10,11,15],particular:1,pascal:4,pass:14,pasta:16,pat:4,patch:[],path:[0,4,18],pattern:[1,14],pb:[1,5],pbe:4,pcid:4,pclmulqdq:4,pd:[0,1,2,3,4,5],pdcm:4,pdpe1gb:4,peb:4,per:[1,3,4],perform:[1,3,4,5,10,11,14,17,18],person:[4,11],pge:4,pip:8,pipelin:[3,6,9,10,13,18,19,21],pixel:[17,18,19],plate:11,pln:4,plot:[0,1,2,3,4,5,14],plot_predictions_vs_ground_truth:4,plot_timeseri:3,plt:[0,1,2,3,4,5],pni:4,point:[1,4],polygon:[1,10],popcnt:4,port:[3,12],posit:[1,13],possibl:11,posterior:5,postfix:3,precalcul:12,precis:[4,15,16],precomput:[],predict:4,prefer:3,prefix:3,preprocess:16,presenc:[11,17],present:11,prettyt:16,previou:[1,3,4,5],previous:14,print:[0,1,2,3,4,5,9],privaci:11,process:[1,6,11,13,14,18,19,21],produc:18,product:14,project:[10,11],propos:[4,11,14],propotyp:11,protocol:12,prototyp:[11,14],provid:[4,11,14,17,19],pse36:4,pse:4,pt:4,pti:4,publish:[14,18,21],puent:17,pygraphviz:16,pyplot:[0,1,2,3,4,5],pytest:16,python:[14,16],pyzmq:16,q_:[],q_lower_left:1,q_lower_right:1,q_total:1,q_upper_left:1,q_upper_right:1,q_winch:1,qthelp:16,qualiti:[4,19],queri:3,quickli:11,r:[4,21],rate:19,rather:18,rdrand:4,rdseed:4,rdtscp:4,re:3,read:[0,2,4,13,14,18,19,20],read_class_nam:20,read_csv:[1,4,5],readi:11,readm:16,real:[1,4],realtim:15,receiv:18,recogn:11,recognit:11,recommed:18,record:[1,3],reduc:[12,14,19],refactor:[],refer:[10,11],regard:11,region:[1,10,11],regist:11,reidentif:[],relat:[],relationship:4,relev:[4,11,14],reli:10,reload:4,remot:11,remov:[0,2,14],render:16,rep_good:4,report:[0,1,2,3,4,5,9],repres:[13,14,18,19],request:16,requir:[5,8,10],rerturn:[],reserv:[],reset_db:3,resiz:2,resize_height:2,resize_width:2,resizer_avg_dt:2,resourc:[10,14],respect:10,restrict:14,result:10,retriev:15,right:1,rise:1,rm:21,ro:11,roi:10,roi_count:1,roi_definition_fil:1,roi_ev:1,roi_events_avg_dt:1,roi_events_filenam:1,roi_events_writ:1,roi_events_writer_avg_dt:1,roi_view:1,roi_view_avg_dt:1,roievent:1,roieventscsvwrit:1,roiobjtest:[],roipresencecount:1,roiview:1,root:3,rover:11,rovervis:11,row:[],rtd:16,rtm:4,run:[4,21],s:[0,1,2,3,4,5,10,11],same:[1,3,4,5],sampl:4,save:[4,5,12],save_img:4,scalabl:3,scenario:4,scene:[11,13,17],scheme:4,scienc:15,scikit:11,scipi:[14,16],scope:10,score:[3,4],screen:1,sdbg:4,seaborn:16,search:[3,10],second:[0,4,14],section:[3,4,9,10,12],see:20,select:[10,14],sep:4,separ:[4,12],sequenc:[4,11,14,19],sequenti:14,seri:3,serializinghtml:16,servic:[11,12,21],set:[4,14],set_connect:[0,1,2,3,4,5,9],set_titl:[1,3],set_xlabel:1,set_ylabel:1,setup:[4,6,13,14,18,19,21],sever:[11,18],shall:4,shape:[1,16],share:[0,14,20],ship:17,should:19,show:[0,2,3,4,5,11,14,17],show_label:[1,4],shutdown:[6,13,14,18,19,21],signal:[11,19],similar:[3,4,11],simpl:[11,14,15],singl:18,sink:[0,1,2,3,4,5,6,9,10,13,14,21],size:[],skip_fram:19,small128:[1,5],smap:4,smep:4,smoke:11,snowballstemm:16,so:4,socket:4,solid:14,solut:14,some:[0,2,10,11,14,18],sort:[4,10,14,15],sourc:[0,1,2,3,4,5,9,10,14],spatial:11,special:10,specif:[1,3,4,5,10,11,12,14,18],specifc:18,specifi:[3,18,19],specyf:4,spent:1,sphinx:[8,16],sphinxcontrib:16,splitext:4,sql:3,src:[0,1,2,3,4,5],ss:4,ssbd:4,sse2:4,sse4_1:4,sse4_2:4,sse:4,ssse3:4,stage:11,stai:17,standard:[4,14],start:[1,11,19],start_fram:[0,1,2,3,4,5,9,19],state:14,statist:[3,14],stats_text:1,step:[0,3,4,14],step_fram:19,stibp:4,store:[1,3,4,14,18],str:[13,14,18,19,20],streamer:21,structur:3,studi:11,style:[0,1,2,3,4,5],subplot:[0,1,2,3,4,5],subset:[],substract:[10,14],succes:14,suitabl:[1,14],support:[0,1,2,3,4,5,14,18,19],sw:11,sy:9,syntax:3,syscal:4,system:11,tail:1,tamper:11,tangon_babor_inf:17,tangon_babor_sup:17,tangon_estribor_inf:17,tangon_estribor_sup:17,task:[4,5,11,14,17,18],tcp:21,techniqu:11,tempor:11,temporari:4,tensorflow:[1,3,4,5,10,15,16],test:[4,17],test_img_seq:4,test_img_seq_path:4,test_output:[0,1,2,3,4,5],test_video:[0,1,2,3,4,5,9],text:[0,1,2,3,4,5,20],textoverlai:1,tf:[1,3,4,5],than:[18,20],thei:10,them:[0,2,11],theme:16,therefor:11,thi:[0,1,2,3,4,5,6,9,10,11,12,13,14,15,18,19,20,21],thing:14,thread:4,through:[12,14],thu:14,time:[0,2,3,5,10,14,17,18],timestamp:3,tini:[1,3,4,5],tm2:4,tm:4,togeth:14,toggl:14,toggle_display_en:14,toml:16,tool:15,top:[],topic:15,topolog:14,total:[0,1,2,3,4,5,14],total_exec_tim:4,total_fram:19,tpr_shadow:4,tqdm:16,track:[10,11,14,15],tracked_obj:13,tracked_objs_filenam:5,trackedobjectsannot:[1,5,13],trackedobjectscsvwrit:[1,5,13],tracker:[1,5,13,17],tracker_annot:[1,5],tracker_annotator_avg_dt:[1,5],tracker_avg_dt:[1,5],tracker_csv_writ:5,tracker_csv_writer_avg_dt:5,tracklet:[],train:4,trajectori:14,transform:10,travers:14,treat:10,trigger:[11,19],tripo:15,truth:4,tsc:4,tsc_adjust:4,tsc_deadline_tim:4,tupl:0,two:[0,3,10,14],txt:[1,3,4,5,8],type:[0,1,2,3,4,5,11,14,19,20],typic:[3,10],under:1,underli:14,uniqu:[13,18,19],unit:[14,19],unless:19,unmatched_detect:[],unmatched_track:[],unset:14,unsuit:4,until:[2,14,19],updat:[14,18],upper:1,upper_left:1,upper_right:1,us:[0,1,2,3,4,5,9,10,11,12,13,14,17,18,19,21],usag:1,util:[4,10],v:1,valid:[],valu:[1,3,19],variabl:[1,3,13,14,18,19],variable_1:18,variable_2:18,variable_list:3,variable_n:18,variablecsvwrit:[1,18],variables_filenam:1,variables_to_publish:3,variables_to_writ:[1,18],variant:[4,12],veloc:13,vendor:4,video:[0,2,3,5,10,14,15,17,18,19],video_fe:21,video_path:[0,1,2,3,4,5,9,19],videoanalyt:[0,1,2,3,4,5,6,8,9,11,12,13,14,18,19,20,21],videofilewrit:4,videoread:[0,1,2,3,4,5,9,19],videoservic:21,videowrit:[0,1,2,3,4,5,9,18],videowriter_fourcc:18,viewer:1,virtual:4,vision:[11,15],visual:[1,4,12,14],vme:4,vmx:4,vnmi:4,voc:4,vpid:4,vt:4,w:[4,5],wa:[0,1,2,3,4,5,11],wai:11,we:[0,1,3,4,5,14],weight:[1,3,4,5],weights_filenam:[1,3,4,5],what:[10,17],when:11,where:[],whether:11,which:[2,4,10,14,17],width:[0,1,2,3,4,5,18,19],wikipedia:15,winch:1,without:[],work:[4,10],workflow:10,worst:14,wrapper:[],write:[0,2,3,13,14,18,19],writer:[0,1,2,3,4,5,9,18],writer_avg_dt:[0,1,2,3,4,5],x0:4,x1:4,x2:[],x2apic:4,x86_64:4,x:[1,4,5],xc:4,xgetbv1:4,xsave:4,xsavec:4,xsaveopt:4,xtopolog:4,xtpr:4,xvid:[0,1,2,4,5,18],xyxi:4,y0:4,y1:4,y2:[],y:[1,4,5],yc:4,yml:8,yolo4:[1,3,4,5],yolo:4,yolo_input_s:[],yolo_iou_threshold:[],yolo_max_output_size_per_class:[],yolo_max_total_s:[],yolo_score_threshold:[],yolov4:[1,3,4,5,10,15],yolov4detectortf:[1,3,4,5],youtub:[0,1,2,3,4,5],zero:[],zeromq:10,zmq:21,zmqpub:21},titles:["A basic pipeline","Events and statistics from ROIs","Image transformation pipeline","Integration with databases","Object detection pipeline","Object tracking pipeline","Background substraction and motion estimation","Integration with databases","Development notes","Examples","Documentation for videoanalytics","Introduction","Object detection","Object tracking","The pipeline paradigm","References and useful resources","&lt;no title&gt;","Working with ROIs","Sinks","Sources","Utilities","Communication with ZeroMQ"],titleterms:{A:[0,1,4],The:14,activ:1,algorithm:5,analyt:11,api:[6,7,12,13,14,17,18,19,20,21],applic:9,background:6,basic:0,commun:21,compon:[4,14],configur:[1,4],content:10,convent:[],count:1,databas:[3,7],deepsort:[5,13],definit:[1,17],depend:8,design:[18,19],detect:[4,12],develop:8,displai:1,document:10,elasticsearch:3,estim:6,evalu:[4,12],event:1,exampl:9,execut:[1,4],explor:[1,3,4,5],format:17,frame:4,from:1,guidelin:[18,19],hello:9,imag:2,implement:12,indic:10,influxdb:3,input:[1,4],insid:1,instanti:[1,4],integr:[3,7],introduct:11,json:17,load:1,manag:8,minim:4,model:4,motion:6,motiv:11,note:8,object:[1,4,5,12,13],organis:14,output:[1,4],paradigm:14,perform:12,pipelin:[0,1,2,4,5,14],polygon:17,refer:[6,7,12,13,14,15,17,18,19,20,21],region:17,resourc:15,result:[1,3,4,5],roi:[1,17],select:4,seri:1,sink:18,sort:[5,13],sourc:19,statist:1,substract:6,tabl:10,tensorflow:12,time:[1,4],track:[5,13],transform:2,trigger:1,typic:0,us:15,util:[12,20],video:[1,4,11],videoanalyt:10,what:11,work:17,workflow:0,world:9,yolov4:12,zeromq:21}})