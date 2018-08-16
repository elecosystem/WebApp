
import mysql.connector
import numpy

class Exercise :

    def __init__(self,id,cirid,types,comp,correct,w):
        self.id = id
        self.cirid = cirid
        self.types = types
        self.comp = comp
        self.correct = correct
        self.w = w

    def detail(self,detail):
        self.detail = detail

    def path(self,img):
        self.img = img


def  genindex():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="CIRCUITDB"
    )

    print(mydb)

    exlist = []
    exercises = mydb.cursor()

    exercises.execute("Select * from EXERCISE")

    for x in exercises:
        # print(x)
        id = x[0]
        cirid = x[1]
        types = x[2]
        comp = x[3]
        correct = x[4]
        w = []
        w.append(x[5])
        w.append(x[6])
        w.append(x[7])
        e = Exercise(id, cirid, types, comp, correct, w)
        exlist.append(e)
    # print(exlist[0])

    # matching exercise with circuit info
    circuit = mydb.cursor()
    print(len(exlist))
    for x in range(0, len(exlist)):
        circuit.execute("Select * from CIRCUIT Where ID='" + str(exlist[x].cirid) + "'")
        result = circuit.fetchall()
        tmpex = exlist[x]
        a = result[0]
        tmpex.detail(a[3])
        tmpex.path(a[2])

        exlist[x] = tmpex

    return exlist

def createQuestion(exercise):
    print(exercise.types)
    quest='Calculate the '
    if exercise.types=='V':
        quest+='voltage drop in'
    elif exercise.types=='I':
        quest+='drawn current in'
    else:
        quest+='power of'

    
    quest+=' '+exercise.comp+'.'

    return quest






#saves exercises

