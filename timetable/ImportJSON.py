# Класс для упрощения работы с базой данных расписания
class ImportJSON:
    def __init__(self):
        import json
        myfile = open('timetable.json', mode='r', encoding='UTF-8')
        data = json.load(myfile)
        myfile.close()
        self.data = data
        courses = set()
        sem = set()
        teachers = set()
        auds = set()
        kabs = set()
        for i in data:
            courses.add(i['course'])
            for j in i['week']:
                sem.add(j['sem'])
                strk=(j['info']['adress'])
                list_strk = strk.split(" ")
                #print(list_strk)
                strk = ""
                for ir in list_strk:
                    strk += ir + "_"
                adress_strk = ""
                for ir in range(0, len(strk) - 1):
                    adress_strk += strk[ir]
                auds.add(adress_strk)
                kabs.add(j['info']['cabinet'])
                if len(i['week'])>0:
                    strk= j['info']['teacher']['lastname']+"_"+j['info']['teacher']['firstname']+"_"+j['info']['teacher']['middlename']
                    teachers.add(strk)
        self.teachers = list(teachers)
        self.courses = list(courses)
        self.adress = list(auds)
        self.cabs = list(kabs)
        self.sem = list(sem)

# Функция получения значений для вывода расписания по группам
    def setTable(self, group, sem):
        data = self.data
        k = 0
        for i in data:
            if i['group'] == group:
                if 'week' in i:
                    week = i['week']
                    k = 1

        if k == 1:

            monday = []
            tuesday = []
            wednesday = []
            thursday = []
            friday = []
            saturday = []

            self.len_1_ch = 0
            self.len_2_ch = 0
            self.len_3_ch = 0
            self.len_4_ch = 0
            self.len_5_ch = 0
            self.len_6_ch = 0
            self.len_1_nch = 0
            self.len_2_nch = 0
            self.len_3_nch = 0
            self.len_4_nch = 0
            self.len_5_nch = 0
            self.len_6_nch = 0

            for i in week:
                if (i['day'] == 'понедельник') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_1_nch+=1
                    else: self.len_1_ch+=1
                    monday.append(i)
                elif (i['day'] == 'вторник') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_2_nch+=1
                    else: self.len_2_ch+=1
                    tuesday.append(i)
                elif (i['day'] == 'среда') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_3_nch+=1
                    else: self.len_3_ch+=1
                    wednesday.append(i)
                elif (i['day'] == 'четверг') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_4_nch+=1
                    else: self.len_4_ch+=1
                    thursday.append(i)
                elif (i['day'] == 'пятница') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_5_nch+=1
                    else: self.len_5_ch+=1
                    friday.append(i)
                elif (i['day'] == 'суббота') & (i['sem'] == sem):
                    if i['chet']=='нечетная':
                        self.len_6_nch+=1
                    else: self.len_6_ch+=1
                    saturday.append(i)
            self.monday = monday
            self.tuesday = tuesday
            self.wednesday = wednesday
            self.thursday = thursday
            self.friday = friday
            self.saturday = saturday

        return k

    # Функция получения значений для вывода расписания по преподавателям
    def SetTableTeacher(self, name, sem):
        FIO = name.split("_")
        week=[]
        data = self.data

        for i in data:
            for j in i['week']:
                if (j['info']['teacher']['firstname'] == FIO[1])&(j['info']['teacher']['middlename'] == FIO[2])&(j['info']['teacher']['lastname'] == FIO[0]):
                    k = j.copy()
                    k.update({'group':i['group']})
                    week.append(k)

        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []
        saturday = []

        self.len_1_ch = 0
        self.len_2_ch = 0
        self.len_3_ch = 0
        self.len_4_ch = 0
        self.len_5_ch = 0
        self.len_6_ch = 0
        self.len_1_nch = 0
        self.len_2_nch = 0
        self.len_3_nch = 0
        self.len_4_nch = 0
        self.len_5_nch = 0
        self.len_6_nch = 0

        for i in week:
            if (i['day'] == 'понедельник') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_1_nch += 1
                else:
                    self.len_1_ch += 1
                monday.append(i)
            elif (i['day'] == 'вторник') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_2_nch += 1
                else:
                    self.len_2_ch += 1
                tuesday.append(i)
            elif (i['day'] == 'среда') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_3_nch += 1
                else:
                    self.len_3_ch += 1
                wednesday.append(i)
            elif (i['day'] == 'четверг') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_4_nch += 1
                else:
                    self.len_4_ch += 1
                thursday.append(i)
            elif (i['day'] == 'пятница') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_5_nch += 1
                else:
                    self.len_5_ch += 1
                friday.append(i)
            elif (i['day'] == 'суббота') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_6_nch += 1
                else:
                    self.len_6_ch += 1
                saturday.append(i)
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

    # Функция получения значений для вывода расписания по аудиториям
    def SetTableAud(self, adress, cab, sem):
        week=[]
        data = self.data

        for i in data:
            for j in i['week']:
                print(j['info']['adress'], "and ", adress)
                print(j['info']['cabinet'], "and ", cab)
                if (j['info']['adress'] == adress)&(j['info']['cabinet']==cab):

                    k = j.copy()
                    k.update({'group':i['group']})
                    print(k)
                    week.append(k)

        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []
        saturday = []

        self.len_1_ch = 0
        self.len_2_ch = 0
        self.len_3_ch = 0
        self.len_4_ch = 0
        self.len_5_ch = 0
        self.len_6_ch = 0
        self.len_1_nch = 0
        self.len_2_nch = 0
        self.len_3_nch = 0
        self.len_4_nch = 0
        self.len_5_nch = 0
        self.len_6_nch = 0
        for i in week:
            if (i['day'] == 'понедельник') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_1_nch += 1
                else:
                    self.len_1_ch += 1
                monday.append(i)
            elif (i['day'] == 'вторник') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_2_nch += 1
                else:
                    self.len_2_ch += 1
                tuesday.append(i)
            elif (i['day'] == 'среда') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_3_nch += 1
                else:
                    self.len_3_ch += 1
                wednesday.append(i)
            elif (i['day'] == 'четверг') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_4_nch += 1
                else:
                    self.len_4_ch += 1
                thursday.append(i)
            elif (i['day'] == 'пятница') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_5_nch += 1
                else:
                    self.len_5_ch += 1
                friday.append(i)
            elif (i['day'] == 'суббота') & (i['sem'] == sem):
                if i['chet'] == 'нечетная':
                    self.len_6_nch += 1
                else:
                    self.len_6_ch += 1
                saturday.append(i)
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        print(week)
