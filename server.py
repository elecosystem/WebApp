# -*- coding: utf-8 -*-
import cherrypy
import mysql.connector
import os
import ExerciseManager as EM


class Root(object):
    
        @cherrypy.expose
        def __init__(self):
            open("home.html","r").read()

        @cherrypy.expose
        def form(self):
            cherrypy.response.headers["Content-Type"] = "text/html"
            return open("form1.html","r").read()

        @cherrypy.expose
        def  index(self):
            print(os.getcwd())
            return  open("home.html","r").read()

        @cherrypy.expose
        def Exercises(self):
            with open('headerexercises', 'r') as myfile:
                head = myfile.read().replace('\n', '')
            print(head)
            exlist = []
            exlist = EM.genindex()
            print(exlist)
            for x in range(0,len(exlist)):
                head = head +"<form method=\"post\" action=\"Question\"> <button type=\"submit\" value=\""+str(exlist[x].id)+"\" name=\"value\" class=\"btn btn-primary\">Exercise"+" "+str(exlist[x].id+1) +"</button></form> "
            head = head + "</div><div class=\"col-sm-2\"></div></div></div></body></html>"
            return head
	
        @cherrypy.expose
        def Question(self,value):
            with open('headerexercicio.html', 'r') as myfile:
                head = myfile.read().replace('\n', '')
            print(head)
            exlist = []
            exlist = EM.genindex()
            print(exlist)
            ans = exlist[int(value)].w
            ans.append(exlist[int(value)].correct)
            a = exlist[int(value)].img;
            img_name = a.split('/')
            img_name = img_name[-1]
            q = EM.createQuestion(exlist[int(value)]);
            head = head +  " "+str(exlist[int(value)].id + 1) + "</h1>"  "<p>" + q+ "</p>"
            head = head +"<p> </<p>"+"<img class=\"mx-auto text-center\" src=images/"+str(img_name)+" height=\"220\ witdh=\"520\">" + "<form>"
            for x in range(0,len(ans)):
                head = head +" <input type=\"radio\" name=\"value\" value=\""+str(ans[x])+"\" >" +str(ans[x]) + " " + str(exlist[int(value)].types) +"<br>"
            head = head + "</form>"
            head = head + "<form method=\"post\" action=\"Exercisees\"> <button type=\"submit\" value=\""+str(value)+"\" name=\"value\" class=\"btn btn-primary\"> Solution </button></form>"+"</div><div class=\"col-sm-2\"></div></div></div></body></html>"
            return head

        @cherrypy.expose
        def Exercisees(self,value):
            with open('headerexercicio.html', 'r') as myfile:
                head = myfile.read().replace('\n', '')
            exlist = []
            exlist = EM.genindex()
            a = exlist[int(value)].img;
            img_name = a.split('/')
            img_name = img_name[-1]
            return head+" "+str(exlist[int(value)].id + 1) + "</h1>" +"<p> </<p>"+"<img class=\"mx-auto text-center\" src=images/"+str(img_name)+" height=\"220\ witdh=\"520\">"+"<p> </p>"+ exlist[int(value)].expl

        @cherrypy.expose
        def Submit(self):
            return  open("Submit.html","r").read()

        @cherrypy.expose
        def Netlist(self):
            return open("netlistsub.html","r").read();

        @cherrypy.expose
        def netsub(self,Netlist):
            size = 0
            all_data=bytearray()
            while True:
                data = Netlist.file.read(8192)
                all_data += data;
                if not data:
                    break
                size += len(data)
                save = open(Netlist.filename,"wb")
                save.write(all_data);

            return open("Image.html","r").read()

        @cherrypy.expose
        def imgsub(self,image):
            size = 0
            all_data=bytearray()
            while True:
                data = image.file.read(8192)
                all_data += data;
                if not data:
                    break
                size += len(data)
                save = open(image.filename,"wb")
                save.write(all_data);

            return open("form1.html","r").read()

        #@cherrypy.expose
        #def subform(self,**kwargs):



if __name__ == "__main__":
    conf = {'/images': {'tools.staticdir.on': True,
                          'tools.staticdir.dir': os.path.join('/home/ele/resources/ExerciseImage')}}
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8888}) #muda a porta para 8081 o 0.0.0.0 significa que ele está à espera de comandos a partir de qualquer interfa$
    cherrypy.quickstart(Root(),'/',config=conf) #lança o servidor




