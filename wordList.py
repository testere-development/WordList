import random
import sys

class WordList:
    def __init__(self):
        # Word List len
        self.WLen=0
        
        
        # LOGO
        
        self.logo ="""\033[35m
        [ TESTERE ]
        --------------
        w o r d l i s t
        ------------aze
        
GitHub: https://github.com/testere-development/WordList
        \033[0m"""
        
        print(self.logo)
        
    
        # VEREBLE
         
    # -------------Max Len--------------------
        self.maxCarakter=input("\nMax Carakter (default 8):")
        
        if not self.maxCarakter:self.maxCarakter=8
            
        else: self.maxCarakter=int(self.maxCarakter)
            
    # ------------Min Len---------------------     
        self.minCarakter=input("\nMin Cakrakter (default 0):")
        
        if not self.minCarakter:self.minCarakter=0
        
        else:self.minCarakter=int(self.minCarakter)
        
    # -----------------Private---------------------
    def crateMy(self,file):

    # --------------My------------------------
        
        self.nickName=input("\nSoyad:").lower()
        
        self.lastName=input("\nLəqəb:").lower()

        while True:
            self.dateBirth=input("\nDoğum Tarixi(il.ay.gün):")
            if self.dateBirth=="" or (len(self.dateBirth)==10 and self.dateBirth.count(".")==2):break
        
    # -------------Mother--------------------
        self.motherName=input("\nAna Adı:").lower()
          
        while True:
            self.dateBirthMother=input("\nAna Doğum Tarixi(il.ay.gün):")
            if self.dateBirthMother=="" or (len(self.dateBirthMother)==10 and self.dateBirthMother.count(".")==2):break
            
    # ----------------Dad-------------------- 
        self.dadName=input("\nAta Adı:").lower()
        
        while True:
            self.dateBirthDad=input("\nAta Doğum Tarixi(il.ay.gün):")
            if self.dateBirthDad=="" or (len(self.dateBirthDad)==10 and self.dateBirthDad.count(".")==2):break
                
    # --------------Wife--------------------- 
        self.wifeName=input("\nYoldaş Adı:").lower()
     
        while True:
            self.dataBirthWife=input("\nYoldaş Doğum Tarixi(il.ay.gün):")
            if self.dataBirthWife=="" or (len(self.dataBirthWife)==10 and self.dataBirthWife.count(".")==2):break
        
    # --------------Child------------------- 
        self.childName=input("\nUşaq Adı:").lower()
        
        while True:
            self.dataBirthChild=input("\nUşaq Doğum Tarixi(il.ay.gün):")
            if self.dataBirthChild=="" or (len(self.dataBirthChild)==10 and self.dataBirthChild.count(".")==2):break
        
    # --------------Pet---------------------
        self.petName=input("\nEv Heyvanı Adı:").lower()

        while True:
            self.petDateBirth=input("\nEv Heyvanı Doğum Tarixi(il.ay.gün):")
            if self.petDateBirth=="" or (len(self.petDateBirth)==10 and self.petDateBirth.count(".")==2):break
            
    # --------------country-----------------   
        self.country=input("\nÖlkə:").lower()
        
    # ---------------City-------------------   
        self.city=input("\nŞəhər/Rayon:").lower()
        
        self.cityNumber=input("\nBölgə Seriyası:").lower()
        
    # ---------------Village----------------
        self.village=input("\nKənd/Qəsəbə:").lower()
        
    # --------------Phone Number------------  
        self.phoneNumber=input("\nTelefon Nömrəsi:").lower()
        
    # --------------Car Number--------------
        self.CarNumber=input("\nMaşın Nömrəsi:").lower()

    # ----------------List+Filter-----------
        
        self.verableList=[
        self.name,self.nickName,
        self.lastName,self.dateBirth,
        self.wifeName,self.dataBirthWife,
        self.childName,self.dataBirthChild,
        self.petName,self.petDateBirth,
        self.country,self.city,self.cityNumber,
        self.phoneNumber,self.CarNumber,
        self.motherName,self.dateBirthMother,
        self.dadName,self.dateBirthDad,self.village
        ]
        
        if self.dateBirth:
            self.verableList.append(self.dateBirth[0:2])                
            self.verableList.append(self.dateBirth[3:5])
            self.verableList.append(self.dateBirth[8:10])
            self.verableList.append(self.dateBirth[6:8])
                
        if self.dataBirthWife:
            self.verableList.append(self.dataBirthWife[0:2])
            self.verableList.append(self.dataBirthWife[3:5])
            self.verableList.append(self.dataBirthWife[8:10])
            self.verableList.append(self.dataBirthWife[6:8])
        
        if self.dataBirthChild:
            self.verableList.append(self.dataBirthChild[0:2])
            self.verableList.append(self.dataBirthChild[3:5])
            self.verableList.append(self.dataBirthChild[8:10])
            self.verableList.append(self.dataBirthChild[6:8])
                
        if self.petDateBirth:
            self.verableList.append(self.petDateBirth[0:2])
            self.verableList.append(self.petDateBirth[3:5])
            self.verableList.append(self.petDateBirth[8:10])
            self.verableList.append(self.petDateBirth[6:8])
                
        if self.dateBirthMother:
            self.verableList.append(self.dateBirthMother[0:2])
            self.verableList.append(self.dateBirthMother[3:5])
            self.verableList.append(self.dateBirthMother[8:10])
            self.verableList.append(self.dateBirthMother[6:8])
                
        if self.dateBirthDad:
            self.verableList.append(self.dateBirthDad[0:2])
            self.verableList.append(self.dateBirthDad[3:5])
            self.verableList.append(self.dateBirthDad[8:10])
            self.verableList.append(self.dateBirthDad[6:8])
        
        self.verableList=list(filter(lambda x: x, self.verableList))
            
        self.verableList = list(dict.fromkeys(self.verableList))
            
        self.end= [
        #
        "123", "1234", "12345", "123456",
        "321", "4321",
        "000", "001", "007",
        "99", "100",
    
        #
        "!", "!!", "!!!",
        "!123", "123!",
        "@", "@123",
        "#1","#",
    
        #
        "qwe", "qwerty", "asd", "asdf", "zxc",
        "1q2w", "q1w2",
    
        # 
        "pass", "admin", "user", "login",
        "pro", "vip", "king", "boss",
        "lol", "omg",
    
        #
        "123!", "1234!", "abc123",
        "a1", "a12", "a123",
        "x1", "z1",
    ]
        
        self.verableList = [a for a in self.verableList if a not in self.end]
    
        
    
    # ------------VerableList Conbination----------------
        if self.verableList:
            for p1 in self.verableList:
                    
                for i in self.end:
                    if self.minCarakter<=len(f"{p1}{i}")<=self.maxCarakter:
                        file.write(f"{p1}{i}\n")
                        file.write(f"{p1.upper()}{i}\n")
                        file.write(f"{p1.capitalize()}{i}\n")
                        
                        self.WLen+=3
                    
                    if self.minCarakter<=len(f"{p1}_{i}")<=self.maxCarakter:
                        file.write(f"{p1}_{i}\n")
                        file.write(f"{p1.upper()}_{i}\n")
                        file.write(f"{p1.capitalize()}_{i}\n")
                        
                        self.WLen+=3
                        
                    if self.minCarakter<=len(f"{p1}.{i}")<=self.maxCarakter:
                        file.write(f"{p1}.{i}\n")
                        file.write(f"{p1.upper()}.{i}\n")
                        file.write(f"{p1.capitalize()}.{i}\n")
                        
                        self.WLen+=3
                        
                    if self.minCarakter<=len(f"{i}{p1}{i}")<=self.maxCarakter:
                        file.write(f"{i}{p1}{i}\n")
                        file.write(f"{i}{p1.upper()}{i}\n")
                        file.write(f"{i}{p1.capitalize()}{i}\n")
                        
                        self.WLen+=3
                        
                    if self.minCarakter<=len(f"{i}{p1}")<=self.maxCarakter:
                        file.write(f"{i}{p1}\n")
                        file.write(f"{i}{p1.upper()}\n")
                        file.write(f"{i}{p1.capitalize()}\n")
                        
                        self.WLen+=3
                        
                    if self.minCarakter<=len(f"{i}_{p1}")<=self.maxCarakter:
                        file.write(f"{i}_{p1}\n")
                        file.write(f"{i}_{p1.upper()}\n")
                        file.write(f"{i}_{p1.capitalize()}\n")
                        
                        self.WLen+=3
                        
                        
                    if self.minCarakter<=len(f"{i}.{p1}")<=self.maxCarakter:
                        file.write(f"{i}.{p1}\n")
                        file.write(f"{i}.{p1.upper()}\n")
                        file.write(f"{i}.{p1.capitalize()}\n")
                        self.WLen+=3
                        
                    if self.minCarakter<=len(f"{i}-{p1}")<=self.maxCarakter:
                        file.write(f"{i}-{p1}\n")
                        file.write(f"{i}-{p1.upper()}\n")
                        file.write(f"{i}-{p1.capitalize()}\n")
                        self.WLen+=3
                
                if self.minCarakter<=len(p1)<=self.maxCarakter:
                    file.write(f"{p1}\n")
                    file.write(f"{p1.upper()}\n")
                    file.write(f"{p1.capitalize()}\n")
                        
                    self.WLen+=3
                    
                for p2 in self.verableList:
                    if self.minCarakter<=len(f"{p1}_{p2}")<=self.maxCarakter:
                        file.write(f"{p1}_{p2}\n")
                        
                        file.write(f"{p1.upper()}_{p2}\n")
                        file.write(f"{p1.capitalize()}_{p2}\n")
                                        
                        file.write(f"{p1}_{p2.upper()}\n")
                        file.write(f"{p1}_{p2.capitalize()}\n")
                        
                        file.write(f"{p1.upper()}_{p2.upper()}\n")
                        file.write(f"{p1.capitalize()}_{p2.capitalize()}\n")
                        
                        self.WLen+=7
                        
                    if self.minCarakter<=len(f"{p1}.{p2}")<=self.maxCarakter:
                        file.write(f"{p1}.{p2}\n")
                        
                        file.write(f"{p1.upper()}.{p2}\n")
                        file.write(f"{p1.capitalize()}.{p2}\n")
                                        
                        file.write(f"{p1}.{p2.upper()}\n")
                        file.write(f"{p1}.{p2.capitalize()}\n")
                        
                        file.write(f"{p1.upper()}.{p2.upper()}\n")
                        file.write(f"{p1.capitalize()}.{p2.capitalize()}\n")
                        
                        self.WLen+=7
                        
                    if self.minCarakter<=len(f"{p1}-{p2}")<=self.maxCarakter:
                        file.write(f"{p1}-{p2}\n")
                        
                        file.write(f"{p1.upper()}-{p2}\n")
                        file.write(f"{p1.capitalize()}-{p2}\n")
                                        
                        file.write(f"{p1}-{p2.upper()}\n")
                        file.write(f"{p1}-{p2.capitalize()}\n")
                        
                        file.write(f"{p1.upper()}-{p2.upper()}\n")
                        file.write(f"{p1.capitalize()}-{p2.capitalize()}\n")
                        
                        self.WLen+=7
                        
                    if self.minCarakter<=len(p1+p2)<=self.maxCarakter:
                        file.write(f"{p1}{p2}\n")
                    
                        file.write(f"{p1.upper()}{p2}\n")
                        file.write(f"{p1.capitalize()}{p2}\n")
                        
                    
                        file.write(f"{p1}{p2.upper()}\n")
                        file.write(f"{p1}{p2.capitalize()}\n")
                        
                    
                        file.write(f"{p1.upper()}{p2.upper()}\n")
                        file.write(f"{p1.capitalize()}{p2.capitalize()}\n")
                        
                        self.WLen+=7
                    
                    for i in self.end:
                        if self.minCarakter<=len(f"{p1}_{p2}{i}")<=self.maxCarakter:
                            file.write(f"{p1}_{p2}{i}\n")
                        
                            file.write(f"{p1.upper()}_{p2}{i}\n")
                            file.write(f"{p1.capitalize()}_{p2}{i}\n")
                                            
                            file.write(f"{p1}_{p2.upper()}{i}\n")
                            file.write(f"{p1}_{p2.capitalize()}{i}\n")
                            
                            file.write(f"{p1.upper()}_{p2.upper()}{i}\n")
                            file.write(f"{p1.capitalize()}_{p2.capitalize()}{i}\n")
                            
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{p1}{p2}{i}")<=self.maxCarakter:
                            file.write(f"{p1}{p2}{i}\n")
                            
                            file.write(f"{p1.upper()}{p2}{i}\n")
                            file.write(f"{p1.capitalize()}{p2}{i}\n")
                                            
                            file.write(f"{p1}{p2.upper()}{i}\n")
                            file.write(f"{p1}{p2.capitalize()}{i}\n")
                            
                            file.write(f"{p1.upper()}{p2.upper()}{i}\n")
                            file.write(f"{p1.capitalize()}{p2.capitalize()}{i}\n")
                        
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{p1}.{p2}{i}")<=self.maxCarakter:
                            file.write(f"{p1}.{p2}{i}\n")
                            
                            file.write(f"{p1.upper()}.{p2}{i}\n")
                            file.write(f"{p1.capitalize()}.{p2}{i}\n")
                                            
                            file.write(f"{p1}.{p2.upper()}{i}\n")
                            file.write(f"{p1}.{p2.capitalize()}{i}\n")
                            
                            file.write(f"{p1.upper()}.{p2.upper()}{i}\n")
                            file.write(f"{p1.capitalize()}.{p2.capitalize()}{i}\n")
                        
                            self.WLen+=7
                            
                        if self.minCarakter<=len(f"{p1}-{p2}{i}")<=self.maxCarakter:
                            file.write(f"{p1}-{p2}{i}\n")
                            
                            file.write(f"{p1.upper()}-{p2}{i}\n")
                            file.write(f"{p1.capitalize()}-{p2}{i}\n")
                                            
                            file.write(f"{p1}-{p2.upper()}{i}\n")
                            file.write(f"{p1}-{p2.capitalize()}{i}\n")
                            
                            file.write(f"{p1.upper()}-{p2.upper()}{i}\n")
                            file.write(f"{p1.capitalize()}-{p2.capitalize()}{i}\n")
                        
                            self.WLen+=7
                            
                        if self.minCarakter<=len(f"{p1}{p2}.{i}")<=self.maxCarakter:
                            file.write(f"{p1}{p2}.{i}\n")
                            
                            file.write(f"{p1.upper()}{p2}.{i}\n")
                            file.write(f"{p1.capitalize()}{p2}.{i}\n")
                                            
                            file.write(f"{p1}{p2.upper()}.{i}\n")
                            file.write(f"{p1}{p2.capitalize()}.{i}\n")
                            
                            file.write(f"{p1.upper()}{p2.upper()}.{i}\n")
                            file.write(f"{p1.capitalize()}{p2.capitalize()}.{i}\n")
                        
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{p1}{p2}_{i}")<=self.maxCarakter:
                            file.write(f"{p1}{p2}_{i}\n")
                            
                            file.write(f"{p1.upper()}{p2}_{i}\n")
                            file.write(f"{p1.capitalize()}{p2}_{i}\n")
                                            
                            file.write(f"{p1}{p2.upper()}_{i}\n")
                            file.write(f"{p1}{p2.capitalize()}_{i}\n")
                            
                            file.write(f"{p1.upper()}{p2.upper()}_{i}\n")
                            file.write(f"{p1.capitalize()}{p2.capitalize()}_{i}\n")
                            
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{p1}{p2}-{i}")<=self.maxCarakter:
                            file.write(f"{p1}{p2}-{i}\n")
                            
                            file.write(f"{p1.upper()}{p2}-{i}\n")
                            file.write(f"{p1.capitalize()}{p2}-{i}\n")
                                            
                            file.write(f"{p1}{p2.upper()}-{i}\n")
                            file.write(f"{p1}{p2.capitalize()}-{i}\n")
                            
                            file.write(f"{p1.upper()}{p2.upper()}-{i}\n")
                            file.write(f"{p1.capitalize()}{p2.capitalize()}-{i}\n")
                        
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{i}{p1}{p2}")<=self.maxCarakter:
                            file.write(f"{i}{p1}{p2}\n")
                            
                            file.write(f"{i}{p1.upper()}{p2}\n")
                            file.write(f"{i}{p1.capitalize()}{p2}\n")
                                            
                            file.write(f"{i}{p1}{p2.upper()}\n")
                            file.write(f"{i}{p1}{p2.capitalize()}\n")
                            
                            file.write(f"{i}{p1.upper()}{p2.upper()}\n")
                            file.write(f"{i}{p1.capitalize()}{p2.capitalize()}\n")
                        
                            self.WLen+=7
                            
                        if self.minCarakter<=len(f"{i}.{p1}{p2}")<=self.maxCarakter:
                            file.write(f"{i}.{p1}{p2}\n")
                            
                            file.write(f"{i}.{p1.upper()}{p2}\n")
                            file.write(f"{i}.{p1.capitalize()}{p2}\n")
                                            
                            file.write(f"{i}.{p1}{p2.upper()}\n")
                            file.write(f"{i}.{p1}{p2.capitalize()}\n")
                            
                            file.write(f"{i}.{p1.upper()}{p2.upper()}\n")
                            file.write(f"{i}.{p1.capitalize()}{p2.capitalize()}\n")
                        
                            self.WLen+=7
                            
                        if self.minCarakter<=len(f"{i}_{p1}{p2}")<=self.maxCarakter:
                            file.write(f"{i}_{p1}{p2}\n")
                            
                            file.write(f"{i}_{p1.upper()}{p2}\n")
                            file.write(f"{i}_{p1.capitalize()}{p2}\n")
                                            
                            file.write(f"{i}_{p1}{p2.upper()}\n")
                            file.write(f"{i}{p1}{p2.capitalize()}\n")
                            
                            file.write(f"{i}_{p1.upper()}{p2.upper()}\n")
                            file.write(f"{i}_{p1.capitalize()}{p2.capitalize()}\n")
                        
                            self.WLen+=7
                        
                        if self.minCarakter<=len(f"{i}-{p1}{p2}")<=self.maxCarakter:
                            file.write(f"{i}-{p1}{p2}\n")
                            
                            file.write(f"{i}-{p1.upper()}{p2}\n")
                            file.write(f"{i}-{p1.capitalize()}{p2}\n")
                                            
                            file.write(f"{i}-{p1}{p2.upper()}\n")
                            file.write(f"{i}-{p1}{p2.capitalize()}\n")
                            
                            file.write(f"{i}-{p1.upper()}{p2.upper()}\n")
                            file.write(f"{i}-{p1.capitalize()}{p2.capitalize()}\n")
                        
                            self.WLen+=7
                            
                            
                        if self.minCarakter<=len(f"{i}{p1}{p2}{i}")<=self.maxCarakter:
                            file.write(f"{i}{p1}{p2}{i}\n")
                            
                            file.write(f"{i}{p1.upper()}{p2}{i}\n")
                            file.write(f"{i}{p1.capitalize()}{p2}{i}\n")
                                            
                            file.write(f"{i}{p1}{p2.upper()}{i}\n")
                            file.write(f"{i}{p1}{p2.capitalize()}{i}\n")
                            
                            file.write(f"{i}{p1.upper()}{p2.upper()}{i}\n")
                            file.write(f"{i}{p1.capitalize()}{p2.capitalize()}{i}\n")
                        
                            self.WLen+=7
                
# -------------VerableList+Year----------------------
    
        for p1 in self.verableList:
            for p2 in range(1900,2050):
                if self.minCarakter<=len(f"{p1}_{p2}")<=self.maxCarakter:
                    file.write(f"{p1}_{p2}\n")
                    file.write(f"{p2}_{p1}\n")
                        
                    file.write(f"{p1.upper()}_{p2}\n")
                    file.write(f"{p2}_{p1.upper()}\n")
                        
                    file.write(f"{p1.capitalize()}_{p2}\n")
                    file.write(f"{p2}_{p1.capitalize()}\n")
                        
                    self.WLen+=6
                        
                if self.minCarakter<=len(f"{p1}{p2}")<=self.maxCarakter:
                    file.write(f"{p1}{p2}\n")
                    file.write(f"{p1.upper()}{p2}\n")
                    file.write(f"{p1.capitalize()}{p2}\n")
                        
                    file.write(f"{p2}{p1}\n")
                    file.write(f"{p2}{p1.upper()}\n")
                    file.write(f"{p2}{p1.capitalize()}\n")                       
                        
                    self.WLen+=6
                        
                if self.minCarakter<=len(f"{p1}.{p2}")<=self.maxCarakter:
                    file.write(f"{p1}.{p2}\n")
                    file.write(f"{p2}.{p1}\n")
                        
                    file.write(f"{p1.upper()}.{p2}\n")
                    file.write(f"{p2}.{p1.upper()}\n")
                        
                    file.write(f"{p1.capitalize()}.{p2}\n")
                    file.write(f"{p2}.{p1.capitalize()}\n")
                        
                    self.WLen+=6
                        
    # -----------------Year+Year-------------------
    def crateYear(self,file):
        if self.maxCarakter>8:
            salt=input("Əlave edilecek (boşluq olmadan yaz tək sətirdə):")

        else:salt=""

        if salt:
            for s in salt:
                for p1 in range(1900,2050):
                    for p2 in range(1900,2050):
                            
                        if self.minCarakter<=len(f"{p1}{p2}{s}")<=self.maxCarakter:
                            file.write(f"{p1}{s}{p2}\n")
                            file.write(f"{p1}{p2}{s}\n")
                            file.write(f"{s}{p1}{p2}\n")
                            file.write(f"{s}{p1}{p2}{s}\n")
                            self.WLen+=4
                            
                        if self.minCarakter<=len(f"{p1}_{p2}{s}")<=self.maxCarakter:
                            file.write(f"{p1}_{p2}{s}\n")
                            file.write(f"{s}{p1}_{p2}\n")
                            file.write(f"{p1}{s}_{p2}\n")
                            file.write(f"{p1}_{s}{p2}\n")
                            file.write(f"{p1}{p2}_{s}\n")
                            self.WLen+=5
                                
                        if self.minCarakter<=len(f"{p1}.{p2}")<=self.maxCarakter:
                            file.write(f"{p1}.{p2}{s}\n")
                            file.write(f"{s}{p1}.{p2}\n")
                            file.write(f"{p1}{s}.{p2}\n")
                            file.write(f"{p1}.{s}{p2}\n")
                            file.write(f"{p1}{p2}.{s}\n")
                            self.WLen+=5
                                
                        if self.minCarakter<=len(f"{p1}-{p2}")<=self.maxCarakter:
                            file.write(f"{p1}.{p2}{s}\n")
                            file.write(f"{s}{p1}.{p2}\n")
                            file.write(f"{p1}{s}.{p2}\n")
                            file.write(f"{p1}.{s}{p2}\n")
                            file.write(f"{p1}{p2}.{s}\n")
                            self.WLen+=5

               
        for p1 in range(1900,2050):
            for p2 in range(1900,2050):
                    
                if self.minCarakter<=len(f"{p1}{p2}")<=self.maxCarakter:
                    file.write(f"{p1}{p2}\n")
                    self.WLen+=1
                    
                if self.minCarakter<=len(f"{p1}_{p2}")<=self.maxCarakter:
                    file.write(f"{p1}_{p2}\n")
                    self.WLen+=1
                        
                if self.minCarakter<=len(f"{p1}.{p2}")<=self.maxCarakter:
                    file.write(f"{p1}.{p2}\n")
                    self.WLen+=1
                        
                if self.minCarakter<=len(f"{p1}-{p2}")<=self.maxCarakter:
                    file.write(f"{p1}-{p2}\n")
                    self.WLen+=1                

    # ----------------End+Son---------------------
    def crateEndStart(self,file):
    
    #-----------Start and End---------
        st=input("Başlanğıc:")
        ed=input("Son:")

    #---------Cohice list--------
        cohice=int(input("1.Rəqəm\n2.Hərf\n3.Rəqəm+Hərf\n=>"))

        match cohice:
            case 1:
                cohiceList="1.2.3.4.5.6.7.8.9.0".split(".")
                
            case 2:
                cohiceList="q.w.e.r.t.y.u.i.o.p.a.s.d.f.g.h.j.k.l.z.x.c.v.b.n.m".split(".")
                for i in cohiceList:cohiceList.append(i.upper())
                
            case 3:
                cohiceList="1.2.3.4.5.6.7.8.9.0".split(".")
                s="q.w.e.r.t.y.u.i.o.p.a.s.d.f.g.h.j.k.l.z.x.c.v.b.n.m".split(".")
                for i in s:cohiceList.append(i.upper());cohiceList.append(i)

        l=self.maxCarakter-len(st)-len(ed)

        k=len(cohiceList)**l

        p=[]
        print(k)

        while True:
            x="".join(random.choices(cohiceList,k=l))

            if not x in p:p.append(x);file.write(f"{st}{x}{ed}\n");self.WLen+=1

            if k==len(p):break



        
        
            

    # ---------------Start------------------------
    def Start(self):
        cohice=int(input("1.Şəxsə özəl\n2.Il+il\n3.Başlanğıc+Random+Son\n=>"))

        match cohice:
            case 1:
                self.name=input("\nAd:").lower()
                self.fileName=self.name+".txt"
                with open(self.fileName,"w") as file:
                    self.crateMy(file)

            case 2:
                self.fileName="yearWordList.txt"
                with open(self.fileName,"w") as file:
                    self.crateYear(file)

            case 3:
                self.fileName="startEnd_WordList.txt"

                with open(self.fileName,"w") as file:
                    self.crateEndStart(file)
                




        print(f"WordList:\n\tFile Name :\033[35m{self.fileName}\033[0m\n\tFile Len:\033[35m{self.WLen}\033[0m")
    
try:
    WordList().Start()

except KeyboardInterrupt:print("\nQuit\n");sys.exit()

except Exception as e:print(f"\033[91m [-]{e}\033[0m")
