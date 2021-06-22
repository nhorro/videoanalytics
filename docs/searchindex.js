Search.setIndex({docnames:["background","devnotes","index","intro","object_detection","object_tracking","pipeline","references","roi","sinks","sources","utils"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,"sphinx.ext.todo":2,sphinx:56},filenames:["background.rst","devnotes.rst","index.rst","intro.rst","object_detection.rst","object_tracking.rst","pipeline.rst","references.rst","roi.rst","sinks.rst","sources.rst","utils.rst"],objects:{"videoanalytics.pipeline":{Sink:[6,1,1,""],Source:[6,1,1,""],process_pipeline:[6,3,1,""],sinks:[9,0,0,"-"],sources:[10,0,0,"-"]},"videoanalytics.pipeline.Sink":{__init__:[6,2,1,""],enable_display:[6,2,1,""],process:[6,2,1,""],setup:[6,2,1,""],shutdown:[6,2,1,""],toggle_display_enable:[6,2,1,""]},"videoanalytics.pipeline.Source":{__init__:[6,2,1,""],read:[6,2,1,""],setup:[6,2,1,""],shutdown:[6,2,1,""]},"videoanalytics.pipeline.sinks":{VideoWriter:[9,1,1,""],background:[0,0,0,"-"],obj_detector:[4,0,0,"-"],roi:[8,0,0,"-"],yolo4_detector:[4,0,0,"-"]},"videoanalytics.pipeline.sinks.VideoWriter":{process:[9,2,1,""],setup:[9,2,1,""],shutdown:[9,2,1,""]},"videoanalytics.pipeline.sinks.background":{BackgroundExtractor1:[0,1,1,""],BackgroundExtractor2:[0,1,1,""]},"videoanalytics.pipeline.sinks.background.BackgroundExtractor1":{process:[0,2,1,""],setup:[0,2,1,""],shutdown:[0,2,1,""]},"videoanalytics.pipeline.sinks.background.BackgroundExtractor2":{process:[0,2,1,""],setup:[0,2,1,""],shutdown:[0,2,1,""]},"videoanalytics.pipeline.sinks.obj_detector":{DetectionsAnnotator:[4,1,1,""],DetectionsCSVWriter:[4,1,1,""],ObjectDetectorCSV:[4,1,1,""]},"videoanalytics.pipeline.sinks.obj_detector.DetectionsAnnotator":{process:[4,2,1,""],setup:[4,2,1,""],shutdown:[4,2,1,""]},"videoanalytics.pipeline.sinks.obj_detector.DetectionsCSVWriter":{process:[4,2,1,""],setup:[4,2,1,""],shutdown:[4,2,1,""]},"videoanalytics.pipeline.sinks.obj_detector.ObjectDetectorCSV":{process:[4,2,1,""],setup:[4,2,1,""],shutdown:[4,2,1,""]},"videoanalytics.pipeline.sinks.roi":{ROIObjTest:[8,1,1,""],ROIView:[8,1,1,""]},"videoanalytics.pipeline.sinks.roi.ROIObjTest":{process:[8,2,1,""],setup:[8,2,1,""],shutdown:[8,2,1,""]},"videoanalytics.pipeline.sinks.roi.ROIView":{process:[8,2,1,""],setup:[8,2,1,""],shutdown:[8,2,1,""]},"videoanalytics.pipeline.sinks.trackers":{sort:[5,0,0,"-"]},"videoanalytics.pipeline.sinks.trackers.sort":{KalmanBoxTracker:[5,1,1,""],SORT:[5,1,1,""],associate_detections_to_trackers:[5,3,1,""],convert_bbox_to_z:[5,3,1,""],convert_x_to_bbox:[5,3,1,""],iou_batch:[5,3,1,""]},"videoanalytics.pipeline.sinks.trackers.sort.KalmanBoxTracker":{__init__:[5,2,1,""],get_state:[5,2,1,""],predict:[5,2,1,""],update:[5,2,1,""]},"videoanalytics.pipeline.sinks.trackers.sort.SORT":{process:[5,2,1,""],setup:[5,2,1,""],shutdown:[5,2,1,""]},"videoanalytics.pipeline.sinks.yolo4_detector":{YOLOv4Detector:[4,1,1,""]},"videoanalytics.pipeline.sinks.yolo4_detector.YOLOv4Detector":{process:[4,2,1,""],setup:[4,2,1,""],shutdown:[4,2,1,""]},"videoanalytics.pipeline.sources":{VideoReader:[10,1,1,""]},"videoanalytics.pipeline.sources.VideoReader":{read:[10,2,1,""],setup:[10,2,1,""],shutdown:[10,2,1,""]},"videoanalytics.utils":{format_boxes:[11,3,1,""],read_class_names:[11,3,1,""]},videoanalytics:{pipeline:[6,0,0,"-"],utils:[11,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function"},terms:{"0":[4,5,10],"1":[5,10],"3":5,"4":4,"416":4,"45":4,"50":4,"abstract":[6,9,10],"case":2,"class":[0,4,5,6,8,9,10,11],"default":[6,9,10],"export":1,"final":6,"function":11,"int":[10,11],"new":9,"return":[5,6,10,11],"true":4,"try":3,A:[6,11],But:3,If:8,It:[3,9],The:[2,4,8,9,10],Their:6,__init__:[5,6],acquir:6,acquisit:10,action:[6,9],activ:[0,4,5,6,8,9],adapt:11,add:[],addit:6,advanc:5,after:[0,4,5,6,8,9,10],algorithm:[3,5],all:[0,4,5,6,8,9,10],allowed_class:4,also:4,altern:4,amount:8,an:[4,6,8,10,11],analyt:2,analyz:3,ani:[4,9],annot:4,api:2,appli:6,ar:[0,2,4,5,6,8,9,10],area:[5,8],arrai:[9,10,11],aspect:5,assign:5,associate_detections_to_track:5,assum:6,attribut:10,audio:10,avail:6,background:2,backgroundextractor1:0,backgroundextractor2:0,base:6,bash:[],basic:2,bb_gt:5,bb_test:5,bbox:[5,11],befor:3,behind:3,being:10,between:5,block:[2,6],both:5,bottom:5,bound:[5,11],box:[5,11],buffer:10,build:[2,6],builid:[],built:9,call:[0,4,5,6,8,9,10],camera:6,can:[6,8,10],cancel:[6,10],captur:10,cartucho:7,categori:4,centr:5,chain:6,class_names_filenam:4,com:7,combin:8,commun:6,complex:9,compon:[0,2,3,5,6,8,10,11],component:[],componnt:[],compos:6,composit:9,compris:2,comput:[5,6],concept:[6,9,10],conda:1,constructor:6,consumpt:4,contain:[6,9,10,11],contempl:10,context:[0,4,5,6,8,9,10],convers:11,convert:11,convert_bbox_to_z:5,convert_x_to_bbox:5,coordin:11,cope:10,core:10,could:[4,10],csv:4,current:[5,10],darknet:[4,11],data:[6,9,11],databas:9,db:6,dedic:[],deep:4,deepsort:[],defin:[3,6],definit:9,depend:[2,4],describ:[2,4],descript:[2,9,10],design:2,detail:[2,3,10],detect:[2,5,7],detectionsannot:4,detectionscsvwrit:4,detector:[4,5,8],develop:2,devic:[6,10],dict:[9,10,11],dictionari:11,differ:10,discuss:2,displai:6,document:1,doe:6,drop:10,each:[0,4,5,6,8,9,11],enable_displai:6,enter:[3,8],entri:[9,10],env:1,environ:1,estim:[2,5,8],etc:8,event:8,exampl:[4,11],execut:6,explor:3,extend:10,extract:3,fast:3,field:[],file:[6,9,10,11],filenam:[4,8,9,10,11],finish:[0,4,5,6,8,9,10],first:[2,4],fledg:3,focu:3,follow:[9,10],follw:2,form:5,format:[4,9,11],format_box:11,fp:[9,10],fragment:10,frame:[6,9,10,11],framer:10,framework:4,freez:1,from:[0,3,4,5,6,8,9,10,11],fulli:3,gener:[1,6],get_stat:5,github:7,global:[9,10],gpu:1,grpc:4,guarante:10,guidelin:2,happen:8,height:[9,10,11],helper:11,here:3,high:10,http:7,id:11,identifi:[],imag:11,image_height:11,image_width:11,implement:[4,5,6,10],includ:4,independ:4,index:2,individu:5,inform:[3,5,6,8,10],initi:5,initialis:5,input:[9,10],input_fp:[9,10],input_height:[9,10],input_width:[9,10],insid:8,insight:8,instanc:[0,4,5,6,8,9,10],integr:3,interest:2,interfac:10,intern:5,intro:[],introduct:2,iou:5,iou_batch:5,iou_threshold:5,its:[2,4],kalmanboxtrack:5,keep:6,learn:4,leav:8,left:5,let:3,librari:[2,3,4],list:5,load:[4,8],make:1,manag:2,map:11,match:5,max_ag:5,max_fram:10,maximum:10,meaning:10,method:[0,2,4,5,6,8,9,10],middlewar:6,might:2,min_hit:5,miscelan:11,model:4,modul:[2,6,9,10,11],more:[2,6,11],most:10,motion:[2,8],motiv:3,movement:[0,8],multipl:11,must:[],naiv:10,name:[1,9,10,11],necesarili:6,none:[5,6,10],normal:11,note:2,np:11,number:[8,10],numpi:[9,10],obj_detector:4,object:[2,7,8],objectdetectorcsv:4,observ:5,obtain:[6,10],one:[6,11],onli:[6,10],opencv:[4,9,10],openlabel:7,oper:6,option:10,order:6,organ:[2,3],other:[4,6,8,10],ouptut:10,output:[6,9],output_format:9,p:6,packag:1,page:2,paradigm:[2,3],paramet:[9,10,11],part:2,perform:[6,9],pip:1,pipelin:[2,9,10],pixel:[9,10,11],polygon:8,port:4,posit:5,precalcul:4,predict:5,presenc:8,previous:6,process:[0,4,5,6,8,9,10],process_pipelin:6,produc:9,product:6,project:2,protocol:4,prototyp:3,provid:[8,10],publish:[6,9],put:3,qualiti:10,r:5,rate:10,ratio:5,read:[6,9,10,11],read_class_nam:11,readi:3,receiv:9,recommed:9,reduc:[4,10],ref:[],refer:2,region:2,relat:4,releg:9,reli:2,repres:[5,9,10],requir:[1,2],resourc:2,respect:2,restrict:6,right:5,roi:2,roiobjtest:8,roiview:8,s:[2,3,5],save:4,scale:5,scene:[5,8],scope:2,score:5,search:2,section:[2,4],see:11,separ:4,sequenc:10,servic:[3,4],set:6,setup:[0,4,5,6,8,9,10],sever:9,share:11,should:10,show_label:4,shutdown:[0,4,5,6,8,9,10],signal:10,simpl:6,sink:[2,6],some:2,sort:6,sourc:[2,6],special:2,specif:[2,4,9],specifc:9,speed:[],sphinx:1,stai:8,start:10,start_fram:10,state:[5,6],step:6,step_fram:10,store:9,str:[9,10,11],substract:2,succes:6,support:[9,10],take:5,task:9,tensorflow:4,test:8,text:11,textfil:11,than:11,thei:2,them:3,thi:[0,2,3,4,5,6,8,9,10,11],thing:6,through:4,time:8,toggl:6,toggle_display_en:6,top:5,topolog:6,total_fram:10,track:2,tracker:8,travers:6,treat:2,two:[2,3,5,6],txt:1,type:[10,11],understand:[],uniqu:5,unit:[6,10],unmatched_detect:5,unmatched_track:5,unset:6,until:[6,10],updat:5,us:[2,3,4,5,6,8,9,10],util:2,valu:10,variabl:[9,10],variant:4,vector:5,veloc:5,video:[2,6,9,10],video_path:10,videoanalyt:[1,9,10],videoread:10,videowrit:9,videowriter_fourcc:9,visual:4,we:6,weights_filenam:4,what:[2,8],where:5,which:[2,8],width:[9,10,11],wip:[],write:[9,10],writer:9,x1:5,x2:5,x:5,xmax:11,xmin:11,xvid:9,y1:5,y2:5,y:5,ymax:11,ymin:11,yml:1,yolo4_detector:[],yolo_input_s:4,yolo_iou_threshold:4,yolo_max_output_size_per_class:4,yolo_max_total_s:4,yolo_score_threshold:4,yolov4:4,yolov4detector:4,z:5},titles:["Background substraction and motion estimation","Development notes","Documentation for videoanalytics","Introduction","Object detection","Object tracking","The pipeline paradigm","References and useful resources","ROIs (regions of interest)","Sinks","Sources","Utilities"],titleterms:{The:6,analyt:3,api:[4,5,6,8,10,11],background:0,compon:[4,9],content:2,deepsort:[],depend:1,design:[9,10],detect:4,develop:1,document:2,estim:0,guidelin:[9,10],implement:[],independ:[],indic:2,interest:8,introduct:3,manag:1,modul:[],motion:0,note:1,obj_detector:[],object:[4,5],paradigm:6,pipelin:[0,4,5,6,8],refer:[4,5,6,7,8,9,10,11],region:8,resourc:7,roi:8,sink:[0,4,5,8,9],sort:5,sourc:10,substract:0,tabl:2,track:5,tracker:5,us:7,util:11,video:3,videoanalyt:[0,2,4,5,6,8,11],what:3,yolo4_detector:4,yolov4:[]}})