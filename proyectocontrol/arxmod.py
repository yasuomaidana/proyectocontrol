class arxM:
     def __init__(self):
         self.ck=[]
         self.mk=[]
         self.pk=[]
         self.inc=0
         self.A=[]
         self.B=[]
         self.d=0
         self.rmk=[]
        
     #lee el archivo y da el orden a la entrada
     def loadmk(self,path):
         f=open(path,"r")
         for i in f:
             if i.isdigit() or '0':
                 self.mk.append(float(i))
         #obtiene las constantes del programa
         f.close()
         return
     def getConst(self,a1,a2,a3,a4,b0,b1,b2,b3,b4,d):
         self.A=[a1,a2,a3,a4]
         self.B=[b0,b1,b2,b3,b4]
         self.d=d
         print(self.A)
         print(self.B)
         print(self.d)
         return
     def getval(self,error):
         print("Entra 2")
         self.pk.append(error)
         print("Entra3")
         c=error
         i=1
         
         for v in self.A:
             if self.val(self.inc-i)<0:
                 c+=0
             else:
                 c+=v*self.ck[self.val(self.inc-i)]
             i+=1
         i=0
         for v in self.B:
             if self.val(self.inc-i-self.d)<0:
                 c+=0
             else:
                 if self.inc-i<len(self.mk):              
                     c+=float(v*self.mk[self.inc-i-self.d])
                 else:
                    c+=float(v*self.mk[len(self.mk)-1])
             i+=1
         
         self.ck.append(c)
         if self.inc<len(self.mk):
            self.rmk.append(float(self.mk[self.inc]))
         else:
            self.rmk.append(float(self.mk[len(self.mk)-1]))
        
         
         self.inc+=1
         return
     def val(self,ind):
         r=ind
         if ind<0:
            r= -1
         return r
