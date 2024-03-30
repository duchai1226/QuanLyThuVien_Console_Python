import json
import sys
class Book:
    def __init__(self,name,author,date):
        self.name=name
        self.author=author
        self.date=date
class Books:
    def __init__(self):
        self.listBook=list()
    def ViewListBook(self):
        print("==========ListBook==========")
        for book in self.listBook:
            print(book.name,book.author,book.date)
    def UpdateBookListFromDB(self):
        with open("db.json","r") as db:
            dbcontent=json.load(db)
        for book in dbcontent["books"]:
            tempbook=Book(book['name'],book['author'],book['date'])
            self.listBook.append(tempbook)
    def UpdateDBJsonFromListBook(self):
        with open("db.json","r") as db:
            dbcontent=json.load(db)
        dbcontent['books'].clear()
        for book in self.listBook:
            dbcontent["books"].append({
                'name':book.name,
                'author':book.author,
                'date':book.date
            })
        with open("db.json",'w') as db:
            json.dump(dbcontent,db,indent=4)
    def AddNewBook(self):
        n=int(input("Ban muon them bao nhieu cuon sach: "))
        if n<1:
            print("Vui long nhap so lon hon 0")
            return
        for i in range(0,n):
            name=input("Nhap ten sach: ")
            author=input("Nhap ten tac gia: ")
            date=input("Nhap ngay: ")
            newbook=Book(name,author,date)
            self.listBook.append(newbook)
        self.UpdateDBJsonFromListBook()
    def Check(self,name,date):
        for temp in self.listBook:
            if temp.name==name and temp.date==date:
                return 1
        return 0
    def Change(self,name,date,choose):
        for i in self.listBook:
            if i.name==name and i.date==date:
                tempbook=Book(i.name,i.author,i.date)
                self.listBook.remove(i)
                if choose==1:
                    newname=input("Moi nhap ten thay doi cho sach: ")
                    tempbook.name=newname
                elif choose==2:
                    newauthor=input("Moi nhap ten tac gia thay doi: ")
                    tempbook.author=newauthor
                elif choose==3:
                    newdate=input("Moi nhap ngay xuat ban thay doi: ")
                    tempbook.date=newdate
                else: 
                    newname=input("Moi nhap ten thay doi cho sach: ")
                    newauthor=input("Moi nhap ten tac gia thay doi: ")
                    newdate=input("Moi nhap ngay xuat ban thay doi: ")
                    tempbook.name=newname
                    tempbook.author=newauthor
                    tempbook.date=newdate
                self.listBook.append(tempbook)

    def ChangeInfoBook(self):
        choose=1
        while(choose!=0):
            self.UpdateDBJsonFromListBook()
            self.ViewListBook()
            name=input("Nhap ten quyen sach muon sua: ")
            date=input("Nhap ngay xuat ban cua quyen sach: ")
            if self.Check(name,date)==0:
                print("===WARNING: Khong tim thay sach can thay doi!===")
                return
            print("=======Change Info Book=======\n1.Change name.\n2.Change Author\n3.Change Date\n4.Change All")
            choose=int(input("Moi nhap lua chon"))
            if choose==1:
                self.Change(name,date,choose)
            elif choose==2:
                self.Change(name,date,choose)
            elif choose==3:
                self.Change(name,date,choose)
            elif choose==4:
                self.Change(name,date,choose)
            else: print("Nhap sai lua chon vui long nhap lai!")
            exit=int(input("Nhap 1 neu muon tiep tuc thay doi, nhap 0 de thoat: "))
            if exit==0: choose=0
    def DeletedBook(self):
        self.ViewListBook()
        name=input("Nhap ten quyen sach muon xoa: ")
        date=input("Nhap ngay xuat ban cua quyen sach muon xoa: ")
        if self.Check(name,date)==0:
            print("===WARNING: Khong tim thay sach can xoa===")
            return
        for book in self.listBook:
            if book.name==name and book.date==date:
                self.listBook.remove(book)
        self.UpdateDBJsonFromListBook()
        print("1")
obj=Books()
obj.UpdateBookListFromDB()
choose=1
while choose!=0:
    print("====================MENU====================\n0.Exit\n1.Coi danh sach\n2.Them sach moi\n3.Sua thong tin 1 quyen sach\n4.Xoa 1 quyen sach")
    choose=int(input("Nhap lua chon: "))
    if choose==1:
        try:
            obj.ViewListBook()
        except FileNotFoundError:
            print("Khong tim thay file")
            sys.exit(0)
        except json.JSONDecodeError:
            print("Loi file JSON")
    elif choose==2:
        try: 
            obj.AddNewBook()
        except ValueError:
            print("Ban can nhap 1 so nguyen ")
            continue
    elif choose==3: 
            obj.ChangeInfoBook()
    elif choose==4:
            obj.DeletedBook()
    elif choose==0:
        print("Exit!")
        sys.exit(0)
    else:
        print("Lua chon khong dung!")
        continue

