import pyodbc
from tkinter import*
from tkinter import messagebox

# Interogarea simpla prin care verific vedem tabelele dupa ce au fost modificate
def interogare(q):
    server = r'DESKTOP-UM2DH23\SQLEXPRESS'
    database = 'Online Cosmetics Shop'
    conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
    # print(conn)
    c=conn.cursor()
    
    
    root2=Tk()

    root2.geometry("1000x800")
    root2.title("Your query result")
    
    queryresult=Label(root2, text="Query result", font=('Arial', 15))
    queryresult.pack()
    
    queryresult1=Label(root2, text=c.execute(q), font=('Arial', 15))
    queryresult1.pack()
    
    for row in c:
        rec=row
        queryresult2=Label(root2, text=rec, font=('Arial', 15))
        queryresult2.pack()
    
    conn.commit()
    c.close()
    conn.close()
    root2.mainloop()



root=Tk()

x1=IntVar()
root.geometry("420x420")
root.title("Login Page Database Project")

# Dupa apasarea butonului de login se verifica username-ul si parola si se trece la partea de modificare de tabele sau vizualizare 
# de interogari
def clicklogin():
    user="admin"
    psww="admin"
    x=x1.get()
    if username.get()== user and password.get()==psww and x==1:
        print("login correct")
        
        root1=Tk()
        root1.geometry("600x600")
        root1.title("Alege Tabela")
        
        # Tabela Angajat cu operatiile care pot fi facute
        def Angajati():
            root2=Tk()
            root2.geometry("600x420")
            root2.title("Tabela Angajat")
            
            def Adaugaangajat():
                n=nume.get()
                p=prenume.get()
                d=int(departament.get())
                s=sex.get()
                c=str(cnp.get())
                s1 = ""
                for i in c:
                    s1 = s1 + str(i)
                print(s1) 
                print(type(s1))
                print(c)
                sal=int(salariu.get())
                
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                values=[(n,p,d,s,s1,sal)]
                c.executemany("INSERT INTO Angajat(Nume,Prenume,DepartamentID,Sex,CNP,Salariu)VALUES(?,?,?,?,?,?)",values)
                conn.commit()
                c.close()
                conn.close()
                
                q1="select* from angajat"
                interogare(q1)
            def Stergeangajat():
                cnps=cnp.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Angajat where cnp=?",cnps)
                conn.commit()
                c.close()
                conn.close()
                q="select* from angajat"
                interogare(q)
            def Modsalangajat():
                cnps=cnp.get()
                sal=salariu.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Angajat SET Salariu=? where CNP=?",(sal,cnps))
                conn.commit()
                c.close()
                conn.close()
                q="select* from angajat"
                interogare(q)
            def Moddepangajat():
                d=departament.get()
                cnps=cnp.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Angajat SET DepartamentID=? where CNP=?",(d,cnps))
                conn.commit()
                c.close()
                conn.close()
                q="select* from angajat"
                interogare(q)
                
                
            numelabel=Label(root2, text="Nume")
            numelabel.grid(row=1,column=0)
            nume=Entry(root2, font=('Arial',15))
            nume.grid(row=1,column=1)
            prenumelabel=Label(root2, text="Prenume")
            prenumelabel.grid(row=1,column=2)
            prenume=Entry(root2, font=('Arial',15))
            prenume.grid(row=1,column=3)
            departamentlabel=Label(root2, text="Departament")
            departamentlabel.grid(row=2,column=0)
            departament=Entry(root2, font=('Arial',15))
            departament.grid(row=2,column=1)
            sexlabel=Label(root2, text="Sex")
            sexlabel.grid(row=2,column=2)
            sex=Entry(root2, font=('Arial',15))
            sex.grid(row=2,column=3)
            cnplabel=Label(root2, text="CNP")
            cnplabel.grid(row=3,column=0)
            cnp=Entry(root2, font=('Arial',15))
            cnp.grid(row=3,column=1)
            salariulabel=Label(root2, text="Salariu")
            salariulabel.grid(row=3,column=2)
            salariu=Entry(root2, font=('Arial',15))
            salariu.grid(row=3,column=3)
            
            adaugaangajat=Button(root2, text="Adauga", command=Adaugaangajat, state=ACTIVE)
            adaugaangajat.place(x=25,y=100)
            stergeangajat=Button(root2, text="Sterge", command=Stergeangajat, state=ACTIVE)
            stergeangajat.place(x=100,y=100)
            modsalangajat=Button(root2, text="Modifica salariu", command=Modsalangajat, state=ACTIVE)
            modsalangajat.place(x=175,y=100)
            moddepangajat=Button(root2, text="Modifica departament", command=Moddepangajat, state=ACTIVE)
            moddepangajat.place(x=300,y=100)
            anunt1=Label(root2, text="ATENTIE! PENTRU STERGERE INTRODUCETI DOAR CNP\nATENTIE! PENTRU MODIFICARE SALARIU INTRODUCETI SALARIU SI CNP\nATENTIE! PENTRU MODIFICARE DEPARTAMENT INTRODUCETI ID-UL DEPARTAMENTULUI SI CNP")
            anunt1.place(x=25,y=140)
            anunt2=Label(root2, text="ID-uri DEPARTAMENTE:\nIT-10\nHR-20\nMARKETING-30\nVANZARI-40")
            anunt2.place(x=25,y=200)
            root2.mainloop()
        
        # Tabela Departament cu operatiile care pot fi facute
        def Departamente():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Tabela Departament")
            
            def Adaugadepartament():
                n=nume.get()
                m=manager.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("INSERT INTO Departament(ManagerID,NumeDepartament)VALUES(?,?)",(m,n))
                conn.commit()
                c.close()
                conn.close()
                q="select* from departament"
                interogare(q)
            def Stergedepartament():
                n=nume.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Departament where NumeDepartament=?",(n))
                conn.commit()
                c.close()
                conn.close()
                q="select* from departament"
                interogare(q)
            def Modnumedepartament():
                n=nume.get()
                m=manager.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Departament SET NumeDepartament=? where ManagerID=?",(n,m))
                conn.commit()
                c.close()
                conn.close()
                q="select* from departament"
                interogare(q)
            def Modmanagerdepartament():
                n=nume.get()
                m=manager.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Departament SET ManagerID=? where NumeDepartament=?",(m,n))
                conn.commit()
                c.close()
                conn.close()
                q="select* from departament"
                interogare(q)
                
            numelabel=Label(root2, text="Nume Departament")
            numelabel.grid(row=1,column=0)
            nume=Entry(root2, font=('Arial',15))
            nume.grid(row=1,column=1)
            managerlabel=Label(root2, text="ID Manager")
            managerlabel.grid(row=2,column=0)
            manager=Entry(root2, font=('Arial',15))
            manager.grid(row=2,column=1)
            
            adaugadep=Button(root2, text="Adauga", command=Adaugadepartament, state=ACTIVE)
            adaugadep.place(x=25,y=100)
            stergedep=Button(root2, text="Sterge", command=Stergedepartament, state=ACTIVE)
            stergedep.place(x=100,y=100)
            modnumedep=Button(root2, text="Modifica nume", command=Modnumedepartament, state=ACTIVE)
            modnumedep.place(x=175,y=100)
            modmandep=Button(root2, text="Modifica manager", command=Modmanagerdepartament, state=ACTIVE)
            modmandep.place(x=300,y=100)
            root2.mainloop()
        
        # Tabela Bon cu operatiile care pot fi efectuate
        def Bonuri():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Tabela Bon")
            
            def Adaugabon():
                cl=clientid.get()
                a=angajatid.get()
                d=data.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("INSERT INTO Bon(ClientID,AngajatID,Data)values(?,?,?)",(cl,a,d))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Bon"
                interogare(q)
            def Stergebon():
                b=idbon.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Bon where BonID=?",(b))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Bon"
                interogare(q)
            def Modangajat():
                a=angajatid.get()
                b=idbon.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Bon SET AngajatID=? where BonID=?",(a,b))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Bon"
                interogare(q)
                
            clientidlabel=Label(root2, text="ClientID")
            clientidlabel.grid(row=1,column=0)
            clientid=Entry(root2, font=('Arial',15))
            clientid.grid(row=1,column=1)
            angajatidlabel=Label(root2, text="AngajatID")
            angajatidlabel.grid(row=2,column=0)
            angajatid=Entry(root2, font=('Arial',15))
            angajatid.grid(row=2,column=1)
            datalabel=Label(root2, text="Data")
            datalabel.grid(row=3,column=0)
            data=Entry(root2, font=('Arial',15))
            data.grid(row=3,column=1)
            idbonlabel=Label(root2, text="BonID")
            idbonlabel.grid(row=4,column=0)
            idbon=Entry(root2, font=('Arial',15))
            idbon.grid(row=4,column=1)

            adaugabon=Button(root2, text="Adauga", command=Adaugabon, state=ACTIVE)
            adaugabon.place(x=25,y=120)
            stergebon=Button(root2, text="Sterge", command=Stergebon, state=ACTIVE)
            stergebon.place(x=100,y=120)
            modangajatid=Button(root2, text="Modifica angajat", command=Modangajat, state=ACTIVE)
            modangajatid.place(x=175,y=120)
            
            root2.mainloop()
        
        # Tabela Client cu operatiile care pot fi efectuate
        def Clienti():
            root2=Tk()
            root2.geometry("600x420")
            root2.title("Tabela Client")
            def Adaugaclient():
                n=nume.get()
                p=prenume.get()
                st=strada.get()
                numar=nr.get()
                o=oras.get()
                j=judet.get()
                cnps=cnp.get()
                s=sex.get()
                
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                values=[(n,p,st,numar,o,j,cnps,s)]
                c.executemany("INSERT INTO Client(Nume,Prenume,Strada,Numar,Oras,Judet,CNP,Sex)VALUES(?,?,?,?,?,?,?,?)",values)
                conn.commit()
                c.close()
                conn.close()
                
                q1="select* from client"
                interogare(q1)
            def Stergeclient():
                cnps=cnp.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Client where cnp=?",cnps)
                conn.commit()
                c.close()
                conn.close()
                q="select* from client"
                interogare(q)
            def Modoras():
                cnps=cnp.get()
                o=oras.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Client SET Oras=? where CNP=?",(o,cnps))
                conn.commit()
                c.close()
                conn.close()
                q="select* from client"
                interogare(q)
            def Modstrada():
                s=strada.get()
                cnps=cnp.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Client SET Strada=? where CNP=?",(s,cnps))
                conn.commit()
                c.close()
                conn.close()
                q="select* from client"
                interogare(q)
            def Modnumar():
                numar=nr.get()
                cnps=cnp.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Client SET Numar=? where CNP=?",(numar,cnps))
                conn.commit()
                c.close()
                conn.close()
                q="select* from client"
                interogare(q)
                
                
            numelabel=Label(root2, text="Nume")
            numelabel.grid(row=1,column=0)
            nume=Entry(root2, font=('Arial',15))
            nume.grid(row=1,column=1)
            prenumelabel=Label(root2, text="Prenume")
            prenumelabel.grid(row=1,column=2)
            prenume=Entry(root2, font=('Arial',15))
            prenume.grid(row=1,column=3)
            stradalabel=Label(root2, text="Strada")
            stradalabel.grid(row=2,column=0)
            strada=Entry(root2, font=('Arial',15))
            strada.grid(row=2,column=1)
            nrlabel=Label(root2, text="Nr.")
            nrlabel.grid(row=2,column=2)
            nr=Entry(root2, font=('Arial',15))
            nr.grid(row=2,column=3)
            oraslabel=Label(root2, text="Oras")
            oraslabel.grid(row=3,column=0)
            oras=Entry(root2, font=('Arial',15))
            oras.grid(row=3,column=1)
            jusetlabel=Label(root2, text="Judet")
            jusetlabel.grid(row=3,column=2)
            judet=Entry(root2, font=('Arial',15))
            judet.grid(row=3,column=3)
            cnplabel=Label(root2, text="CNP")
            cnplabel.grid(row=4,column=0)
            cnp=Entry(root2, font=('Arial',15))
            cnp.grid(row=4,column=1)
            sexlabel=Label(root2, text="Sex")
            sexlabel.grid(row=4,column=2)
            sex=Entry(root2, font=('Arial',15))
            sex.grid(row=4,column=3)
            
            adaugaangajat=Button(root2, text="Adauga", command=Adaugaclient, state=ACTIVE)
            adaugaangajat.place(x=25,y=120)
            stergeangajat=Button(root2, text="Sterge", command=Stergeclient, state=ACTIVE)
            stergeangajat.place(x=100,y=120)
            modsalangajat=Button(root2, text="Modifica oras", command=Modoras, state=ACTIVE)
            modsalangajat.place(x=175,y=120)
            moddepangajat=Button(root2, text="Modifica strada", command=Modstrada, state=ACTIVE)
            moddepangajat.place(x=275,y=120)
            moddepangajat=Button(root2, text="Modifica numar", command=Modnumar, state=ACTIVE)
            moddepangajat.place(x=400,y=120)
            anunt1=Label(root2, text="ATENTIE! PENTRU STERGERE INTRODUCETI DOAR CNP\nATENTIE! PENTRU MODIFICARE ORAS INTRODUCETI ORAS SI CNP\nATENTIE! PENTRU MODIFICARE STRADA INTRODUCETI STRADA SI CNP\nATENTIE! PENTRU MODIFICARE NUMAR INTRODUCETI NUMAR SI CNP")
            anunt1.place(x=25,y=150)
            root2.mainloop()
        
        # Tabela Comanda cu operatiile aferente
        def Comenzi():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Tabela Comanda")
            
            def Adaugacomanda():
                b=bonid.get()
                p=produsid.get()
                n=nrbuc.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("INSERT INTO Comanda(BonID,ProdusID,Nr_bucati)values(?,?,?)",(b,p,n))
                conn.commit()
                c.close()
                conn.close()
                q="select* from comanda"
                interogare(q)
            def Stergecomanda():
                cid=comandaid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Comanda where cid=?",cid)
                conn.commit()
                c.close()
                conn.close()
                q="select* from comanda"
                interogare(q)
            def Modprodusid():
                cid=comandaid.get()
                p=produsid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Comanda SET Produsid=? where ComandaID=?",(p,cid))
                conn.commit()
                c.close()
                conn.close()
                q="select* from comanda"
                interogare(q)
            def Modnrbuc():
                cid=comandaid.get()
                n=nrbuc.get()
                p=produsid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Comanda SET Nr_bucati=? where ComandaID=? and ProdusID=?",(n,cid,p))
                conn.commit()
                c.close()
                conn.close()
                q="select* from comanda"
                interogare(q)
            
            bonidlabel=Label(root2, text="BonID")
            bonidlabel.grid(row=1,column=0)
            bonid=Entry(root2, font=('Arial',15))
            bonid.grid(row=1,column=1)
            produsidlabel=Label(root2, text="ProdusID")
            produsidlabel.grid(row=2,column=0)
            produsid=Entry(root2, font=('Arial',15))
            produsid.grid(row=2,column=1)
            nrbuclabel=Label(root2, text="Nr. bucati")
            nrbuclabel.grid(row=3,column=0)
            nrbuc=Entry(root2, font=('Arial',15))
            nrbuc.grid(row=3,column=1)
            comandaidlabel=Label(root2, text="ComandaID")
            comandaidlabel.grid(row=4,column=0)
            comandaid=Entry(root2, font=('Arial',15))
            comandaid.grid(row=4,column=1)
            
            
            adaugacomanda=Button(root2, text="Adauga", command=Adaugacomanda, state=ACTIVE)
            adaugacomanda.place(x=25,y=120)
            stergecomanda=Button(root2, text="Sterge", command=Stergecomanda, state=ACTIVE)
            stergecomanda.place(x=100,y=120)
            modprodusid=Button(root2, text="Modifica produsid", command=Modprodusid, state=ACTIVE)
            modprodusid.place(x=175,y=120)
            modnrbuc=Button(root2, text="Modifica nrbuc", command=Modnrbuc, state=ACTIVE)
            modnrbuc.place(x=300,y=120)
            root2.mainloop()
        
        # Tabela Produs cu cele 4 operatii posibile care pot fi facute asupra ei
        def Produse():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Tabela Produs")
            
            def Adaugaprodus():
                cid=categorieid.get()
                n=nume.get()
                p=pret.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("INSERT INTO Produs(CategorieID,NumeProdus,Pret)values(?,?,?)",(cid,n,p))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Produs"
                interogare(q)
            def Stergeprodus():
                n=nume.add()
                pr=produsid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Produs where ProdusID=? and NumeProdus=?",(pr,n))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Produs"
                interogare(q)
            def Modnumeprodus():
                n=nume.get()
                pr=produsid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Produs SET NumeProdus=? where ProdusID=?",(n,pr))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Produs"
                interogare(q)
            def Modpret():
                pr=produsid.get()
                p=pret.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Produs SET Pret=? where ProdusID=?",(p,pr))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Produs"
                interogare(q)
                
            
            categorieidlabel=Label(root2, text="CategorieID")
            categorieidlabel.grid(row=1,column=0)
            categorieid=Entry(root2, font=('Arial',15))
            categorieid.grid(row=1,column=1)
            numelabel=Label(root2, text="Nume Produs")
            numelabel.grid(row=2,column=0)
            nume=Entry(root2, font=('Arial',15))
            nume.grid(row=2,column=1)
            pretlabel=Label(root2, text="Pret")
            pretlabel.grid(row=3,column=0)
            pret=Entry(root2, font=('Arial',15))
            pret.grid(row=3,column=1)
            produsidlabel=Label(root2, text="ProdusID")
            produsidlabel.grid(row=4,column=0)
            produsid=Entry(root2, font=('Arial',15))
            produsid.grid(row=4,column=1)
            
            adaugaprodus=Button(root2, text="Adauga", command=Adaugaprodus, state=ACTIVE)
            adaugaprodus.place(x=25,y=120)
            stergeprodus=Button(root2, text="Sterge", command=Stergeprodus, state=ACTIVE)
            stergeprodus.place(x=100,y=120)
            modnumeprodus=Button(root2, text="Modifica nume produs", command=Modnumeprodus, state=ACTIVE)
            modnumeprodus.place(x=165,y=120)
            modpret=Button(root2, text="Modifica pret", command=Modpret, state=ACTIVE)
            modpret.place(x=305,y=120)
            root2.mainloop()
        
        # Tabela categorie cu cele 4 operatii pe care le pot face pe ea 
        def Categorii():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Tabela Categorie")
            
            def Adaugacategorie():
                n=numecat.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("INSERT INTO Categorie(NumeCategorie)",n)
                conn.commit()
                c.close()
                conn.close()
                q="select* from Categorie"
                interogare(q)
            def Stergecategorie():
                n=numecat.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("DELETE FROM Categorie where NumeCategorie=?",n)
                conn.commit()
                c.close()
                conn.close()
                q="select* from Categorie"
                interogare(q)
            def Modnumecategorie():
                n=numecat.get()
                catid=catid.get()
                server = r'DESKTOP-UM2DH23\SQLEXPRESS'
                database = 'Online Cosmetics Shop'
                conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
                c=conn.cursor()
                c.execute("UPDATE Categorie SET NumeCategorie=? where CategorieID=?",(n,catid))
                conn.commit()
                c.close()
                conn.close()
                q="select* from Categorie"
                interogare(q)
            
            numecatlabel=Label(root2, text="Nume Categorie")
            numecatlabel.grid(row=1,column=0)
            numecat=Entry(root2, font=('Arial',15))
            numecat.grid(row=1,column=1)
            catidlabel=Label(root2, text="Categorie ID")
            catidlabel.grid(row=2,column=0)
            catid=Entry(root2, font=('Arial',15))
            catid.grid(row=2,column=1)
            
            adaugacategorie=Button(root2, text="Adauga", command=Adaugacategorie, state=ACTIVE)
            adaugacategorie.place(x=25,y=120)
            stergecategorie=Button(root2, text="Sterge", command=Stergecategorie, state=ACTIVE)
            stergecategorie.place(x=100,y=120)
            modnumecategorie=Button(root2, text="Modifica nume categorie", command=Modnumecategorie, state=ACTIVE)
            modnumecategorie.place(x=165,y=120)
            root2.mainloop()
            
        # Cele 7 tabele pe care putem sa le modificam aplicand anumite operatii pe ele    
        label=Label(root1,text="\nALEGE TABELA", font=('Arial', 15, 'bold'))
        label.grid(row=0,column=1)
        Angajati=Button(root1, text="Angajati", command=Angajati, state=ACTIVE)
        Angajati.grid(row=1,column=3)
        Departamente=Button(root1, text="Departamente", command=Departamente, state=ACTIVE)
        Departamente.grid(row=3,column=3)
        Bonuri=Button(root1, text="Bonuri", command=Bonuri, state=ACTIVE)
        Bonuri.grid(row=5,column=3)
        Clienti=Button(root1, text="Clienti", command=Clienti, state=ACTIVE)
        Clienti.grid(row=7,column=3)
        Comenzi=Button(root1, text="Comenzi", command=Comenzi, state=ACTIVE)
        Comenzi.grid(row=9,column=3)
        Produse=Button(root1, text="Produse", command=Produse, state=ACTIVE)
        Produse.grid(row=11,column=3)
        Categorii=Button(root1, text="Categorii", command=Categorii, state=ACTIVE)
        Categorii.grid(row=13,column=3)
        
        # Enunturile celor 10 interogari pe care le-am facut
        def enunturi():
            root2=Tk()
            root2.geometry("1000x800")
            root2.title("Enunturi")
            label1=Label(root2,text="\nEnunturile interogarilor efectuate sunt urmatoarele:\n\n1.Afisati angajatii care au salariul mai mare decat cel al managerului departamentului din care fac parte.", font=('Arial', 10, 'bold'))
            label1.grid(row=1,column=0)
            label2=Label(root2,text="\n2.Afisati pentru fiecare department numarul angajatilor si media salariilor angajatilor pentru toate departamentele.", font=('Arial', 10, 'bold'))
            label2.grid(row=2,column=0)
            label3=Label(root2,text="\n3.Sa se gaseasca cele mai mari 3 salarii ale angajatilor ce lucreaza pentru departamentul “IT”.", font=('Arial', 10, 'bold'))
            label3.grid(row=3,column=0)
            label4=Label(root2,text="\n4.Sa se afiseze numele angajatului o singura data si \nnumele departamentului din care face parte angajatul de pe fiecare bon.", font=('Arial', 10, 'bold'))
            label4.grid(row=4,column=0)
            label5=Label(root2,text="\n5.Sa se afiseze pretul mediu pentru fiecare categorie de produse.", font=('Arial', 10, 'bold'))
            label5.grid(row=5,column=0)
            label6=Label(root2,text="\n6.Sa se afiseze numele, prenumele si departamentul fiecarui manager de departament.", font=('Arial', 10, 'bold'))
            label6.grid(row=6,column=0)
            label7=Label(root2,text="\n7.Sa se afiseze angajatii cu cel mai mare salariu pentru fiecare departament.\n Ordonati in ordinea descrescatoare a salariului.", font=('Arial', 10, 'bold'))
            label7.grid(row=7,column=0)
            label8=Label(root2,text="\n8.Sa se afiseze cele mai recente bonuri de la fiecare angajat. \nOrdonati dupa data emiterii.", font=('Arial', 10, 'bold'))
            label8.grid(row=8,column=0)
            label9=Label(root2,text="\n9.Sa se afiseze departamentele fara angajati.", font=('Arial', 10, 'bold'))
            label9.grid(row=9,column=0)
            label10=Label(root2,text="\n10.Sa se afiseze numele, prenumele, salariul si numele departamentului la care lucreaza pentru \norice angajat care castiga un salariu mai mare decat media pentru departamentul din care face parte.", font=('Arial', 10, 'bold'))
            label10.grid(row=10,column=0)
            root2.mainloop()
        
        # Cele 10 interogari
        def Interogare1():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 1")
            q='''SELECT A.Nume, A.Prenume, A.Salariu 
            FROM Angajat A 
	        INNER JOIN Departament D ON D.DepartamentID = A.DepartamentID
	        INNER JOIN Angajat AM  ON D.ManagerID = AM.AngajatID
	        WHERE A.Salariu > AM.Salariu'''
            
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare2():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 2")
            q='''SELECT D.NumeDepartament, COUNT(A.AngajatID) AS NrAngajati, 
            AVG(A.Salariu) AS MedieSalariu FROM Departament D LEFT JOIN Angajat A
            ON A.DepartamentID = D.DepartamentID
            GROUP BY D.NumeDepartament'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare3():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 3")
            q='''SELECT TOP 3 A.Salariu
            From Angajat A INNER JOIN Departament D ON A.DepartamentID = D.DepartamentID
            WHERE D.NumeDepartament = 'IT'
            ORDER BY A.Salariu DESC'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare4():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 4")
            q='''SELECT  distinct a.nume AS nume_angajat, d.NumeDepartament AS nume_departament
            FROM bon
            JOIN angajat a ON bon.AngajatID = a.AngajatID
            JOIN departament d ON a.DepartamentID = d.DepartamentID;'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare5():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 5")
            q='''SELECT distinct c.NumeCategorie AS nume_categorie, AVG(p.Pret) AS pret_mediu
            FROM produs p
            JOIN categorie c ON p.CategorieID = c.CategorieID
            GROUP BY c.NumeCategorie'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare6():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 6")
            q='''SELECT a.nume,a.prenume, d.NumeDepartament AS nume_departament
            FROM angajat a
            JOIN departament d ON a.AngajatID = d.ManagerID;'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
        
        def Interogare7():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 7")
            q='''SELECT a.nume, a.prenume, a.salariu, a.DepartamentID
            FROM angajat a
            WHERE a.salariu IN
            (SELECT max(a2.salariu) FROM angajat a2
            WHERE a2. departamentID=a.departamentID)
            ORDER BY a.salariu DESC'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
        
        def Interogare8():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 8")
            q='''SELECT BonID, AngajatID, data
            FROM bon
            WHERE (data) IN
            (SELECT max(b2.data) FROM bon b2
            WHERE b2.AngajatID=bon.AngajatID
            GROUP BY AngajatID)
            ORDER BY data'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
        
        def Interogare9():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 9")
            q='''SELECT DepartamentID, NumeDepartament
            FROM Departament D
            WHERE (SELECT count(*) FROM angajat a WHERE a.DepartamentID=D. DepartamentID)=0'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
            
        def Interogare10():
            root2=Tk()
            root2.geometry("420x420")
            root2.title("Interogare 10")
            q='''SELECT a.nume, a.prenume, a.salariu,d.NumeDepartament
            FROM angajat a INNER JOIN Departament d ON a.DepartamentID = d.DepartamentID 
            WHERE salariu > (SELECT avg(salariu) 
				             FROM angajat
				             WHERE a.departamentID = angajat.departamentID) 
            ORDER BY a.salariu DESC'''
        
            server = r'DESKTOP-UM2DH23\SQLEXPRESS'
            database = 'Online Cosmetics Shop'
            conn = pyodbc.connect('DRIVER={SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
            c=conn.cursor()
            rez=c.execute(q)
            print(rez)
            queryresult=Label(root2, text="Query result", font=('Arial', 15))
            queryresult.pack()
            for row in rez:
                rec=row
                queryresult2=Label(root2, text=rec, font=('Arial', 15))
                queryresult2.pack()
            conn.commit()
            c.close()
            conn.close()
            root2.mainloop()
        
        #Butoanele pentru cele 10 interogari, primele 6 sunt cele simple iar ultimele 4 sunt cele complexe
        label=Label(root1,text="\nINTEROGARI", font=('Arial', 15, 'bold'))
        label.grid(row=14,column=1)
        enunturi=Button(root1, text="Enunturi interogari", command=enunturi, state=ACTIVE)
        enunturi.grid(row=15,column=3)
        Interogare1=Button(root1, text="Interogare 1", command=Interogare1, state=ACTIVE)
        Interogare1.grid(row=16,column=3)
        Interogare2=Button(root1, text="Interogare 2", command=Interogare2, state=ACTIVE)
        Interogare2.grid(row=17,column=3)
        Interogare3=Button(root1, text="Interogare 3", command=Interogare3, state=ACTIVE)
        Interogare3.grid(row=18,column=3)
        Interogare4=Button(root1, text="Interogare 4", command=Interogare4, state=ACTIVE)
        Interogare4.grid(row=19,column=3)
        Interogare5=Button(root1, text="Interogare 5", command=Interogare5, state=ACTIVE)
        Interogare5.grid(row=20,column=3)
        Interogare6=Button(root1, text="Interogare 6", command=Interogare6, state=ACTIVE)
        Interogare6.grid(row=21,column=3)
        Interogare7=Button(root1, text="Interogare 7", command=Interogare7, state=ACTIVE)
        Interogare7.grid(row=22,column=3)
        Interogare8=Button(root1, text="Interogare 8", command=Interogare8, state=ACTIVE)
        Interogare8.grid(row=23,column=3)
        Interogare9=Button(root1, text="Interogare 9", command=Interogare9, state=ACTIVE)
        Interogare9.grid(row=24,column=3)
        Interogare10=Button(root1, text="Interogare 10", command=Interogare10, state=ACTIVE)
        Interogare10.grid(row=25,column=3)
        
        root1.mainloop()
    else:
        messagebox.showinfo(title="Error", message="Make sure you are not a robot\nYour username or password is invalid")
        
        

label=Label(root,text="\nLogin Page", font=('Arial', 30, 'bold'))
label.grid(row=0,column=1)



usernamelabel=Label(root, text="Username")
usernamelabel.grid(row=1,column=0)
username=Entry(root, font=('Arial',15))
username.grid(row=1,column=1)




passwordlabel=Label(root, text="Password")
passwordlabel.grid(row=2,column=0)
password=Entry(root, font=('Arial',15), show="*")
password.grid(row=2,column=1)




checkbox=Checkbutton(root, text="I'm not a robot",font=('Ariel', 10), variable=x1, onvalue=1, offvalue=0, padx=25, pady=10)
checkbox.grid(row=3,column=1)
loginbutton=Button(root, text="Login", command=clicklogin, state=ACTIVE)
loginbutton.grid(row=4, column=1)



root.mainloop()