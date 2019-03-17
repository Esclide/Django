from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .ImportJSON import *
from .Functions import *


# Обработка страницы добавленя группы/предмета в расписание
def setSubject(request):
    if (request.session.has_key('access')):
        if (request.session['access'] == "Manager") | (request.session['access'] == "Admin"):
            if (request.GET):
                if 'sub' in request.GET:
                    group_num = request.GET["group_num"]
                    day = request.GET["day"]
                    chet = request.GET["chet"]
                    time = request.GET["time"]
                    note = request.GET["note"]
                    sem = request.GET['sem']
                    adress = request.GET["adress"]
                    aud = request.GET["aud"]
                    sub = request.GET["subject"]
                    type = request.GET["type"]
                    print('SUB = ', sub)
                    FIO = ((request.GET["FIO"]).split())
                    info1 = {'day': day,
                            'chet': chet,
                            'time': time,
                            'sem': sem,
                            'note': note,
                            'info':{'adress':adress,
                                    'cabinet':aud,
                                    'subject':{'name':sub,
                                               'type':type
                                               },
                                    'teacher':{'firstname':FIO[1],
                                               'middlename':FIO[2],
                                               'lastname':FIO[0]}
                                    }
                            }
                    k1 = WriteDay('timetable.json', group_num, **info1)
                if 'group' in request.GET:
                    course = request.GET["course"]
                    facult = request.GET["facult"]
                    groups = request.GET["groups"]
                    info2 = {'course': course,
                            'facult': facult,
                            'group': groups,
                            'week': []}
                    k2 = WriteGroup('timetable.json', **info2)

            file = ImportJSON()
            return render(request, 'setSubject.html',locals())
        else:
            return (enter(request))
    else:
        return (enter(request))

# Обработка страницы авторизации
def enter(request):
    import hashlib
    try:
        del request.session['access']
        del request.session['login']
    except:
        pass
    if (request.POST):
        login = request.POST["login"]
        password = request.POST["password"]
        b = bytes(password, 'utf-8')
        h = hashlib.sha1(b)
        password = h.hexdigest()
        k=CheckAcc('Authorisation.json', login, password)

        if (k == 'Manager'):
            access = k
            request.session['access'] = access
            request.session['login'] = login
            return render(request, 'FirstPage.html', {"access" : access, 'login': login})
        elif (k == 'Admin'):
            access = k
            request.session['access'] = access
            request.session['login'] = login
            return render(request, 'FirstPage.html', {"access" : access, 'login': login})
        else:
            k="None"
            return render(request, 'Enter.html', locals())
    else: return render(request, 'Enter.html', locals())

# Обработка главной страницы
def start(request):
    if (request.session.has_key('access')):
        if (request.session['access'] == "Manager")|(request.session['access'] == "Admin"):
            login = request.session['login']
            return render(request, 'FirstPage.html', locals())
        else:
            return (enter(request))
    else:return (enter(request))


# Обработка страницы удаления расписания или группы
def delSubject(request):
    import json
    if (request.session.has_key('access')):
        if (request.session['access'] == "Manager") | (request.session['access'] == "Admin"):
            if (request.GET):
                file = ImportJSON()
                if 'sub' in request.GET:
                    group_num = request.GET["group_num"]
                    day = request.GET["day"]
                    chet = request.GET["chet"]
                    time = request.GET["time"]
                    sem = request.GET['sem']
                    info = {'day': day,
                            'chet': chet,
                            'sem':sem,
                            'time': time}
                    myfile = open('timetable.json', mode='r', encoding='UTF-8')
                    data = json.load(myfile)
                    myfile.close()

                    k = 0

                    l = 0
                    k = 0
                    m=0
                    for i in data:
                        if (i['group'] == group_num):
                            if 'week' in i:
                                for j in i['week']:
                                    if ((j['day'] == info['day']) & (j['chet'] == info['chet']) & (
                                            j['time'] == info['time'])&(j['sem']==info['sem'])):
                                        del data[l]['week'][k]
                                        m=1
                                        break
                                    k += 1
                        l += 1
                    myfile2 = open('timetable.json', mode='w', encoding='UTF-8')
                    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
                    myfile2.close()
                if 'group' in request.GET:
                    group = request.GET['groups']
                    myfile = open('timetable.json', mode='r', encoding='UTF-8')
                    data = json.load(myfile)
                    myfile.close()
                    k = 0
                    for i in data:
                        if (i['group'] == group):
                            print(i['group'], 'and ', group)
                            del data[k]
                            l = 1
                        k += 1

                    myfile2 = open('timetable.json', mode='w', encoding='UTF-8')
                    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
                    myfile2.close()
                if 'clear' in request.GET:
                    group = request.GET['group_clear']
                    myfile = open('timetable.json', mode='r', encoding='UTF-8')
                    data = json.load(myfile)
                    myfile.close()
                    k = 0
                    for i in data:
                        if (i['group'] == group):
                            course = i['course']
                            facult = i['facult']
                            print(i['group'], 'and ', group)
                            del data[k]
                        k += 1

                    myfile2 = open('timetable.json', mode='w', encoding='UTF-8')
                    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
                    myfile2.close()
                    info2 = {'course': course,
                             'facult': facult,
                             'group': group,
                             'week': []}
                    k2 = WriteGroup('timetable.json', **info2)


            file = ImportJSON()
            return render(request, 'delSubject.html', locals())
        else:
            return (enter(request))
    else:
        return (enter(request))

# Обработка страницы смена пароля
def ChangePassword(request):
    import hashlib
    if (request.session.has_key('access')):
        login = request.session['login']
        if (request.session['access'] == "Admin"):
            ky=1
        elif (request.session['access'] == "Manager"):
            ky=0
        if (request.POST):
            old_password=request.POST["old"]
            b = bytes(old_password, 'utf-8')
            h = hashlib.sha1(b)
            old_password = h.hexdigest()
            new_password = request.POST["new"]
            b = bytes(new_password, 'utf-8')
            h = hashlib.sha1(b)
            new_password = h.hexdigest()
            repeat = request.POST["repeat"]
            b = bytes(repeat, 'utf-8')
            h = hashlib.sha1(b)
            repeat = h.hexdigest()
            if new_password!=repeat:
                k = 3
                return render(request, 'Set.html', locals())
            else:

                access = request.session['access']
                k =SetPassword(old_password, new_password, login, access)
                return render(request, 'Set.html', locals())
        else: return render(request, 'Set.html', locals())

    else:
        return (enter(request))

# Обработка страницы вывода расписания по группам
def timetable_groups(request):
	if (request.session.has_key('access')):
		file = ImportJSON()
		if (request.GET):
			group = request.GET['group_num']
			sem = request.GET['sem']
			k = file.setTable(group, sem)

		return render(request, 'timetable_groups.html', locals())
	else:return (enter(request))

# Обработка страницы вывода расписания по преподавателям
def timetable_prepod(request):
	if (request.session.has_key('access')):
		file = ImportJSON()
		if (request.GET):
			teacher = request.GET['teacher']
			sem = request.GET['sem']
			t_list = teacher.split('_')
			str_teacher=''
			for i in t_list:
				str_teacher+=i+" "
			file.SetTableTeacher(teacher, sem)
			k=1
		return render(request, 'timetable_teachers.html', locals())
	else:return (enter(request))

# Обработка страницы вывода расписания по аудиториям
def timetable_aud(request):
    if (request.session.has_key('access')):
        file = ImportJSON()
        if (request.GET):
            adress = request.GET['adress']
            cab = request.GET['cab']
            sem = request.GET['sem']
            t_list = adress.split('_')
            str_adress = ''
            for i in t_list:
                str_adress += i + " "
            adress_strk = ""
            for ir in range(0, len(str_adress) - 1):
                adress_strk += str_adress[ir]
            file.SetTableAud(adress_strk, cab, sem)
            k=1
        return render(request, 'timetable_auds.html', locals())
    else:return (enter(request))

# Обработка страницы вывода гостевой версии расписания по группам
def timetable_gost(request):
        file = ImportJSON()
        if (request.GET):
            group = request.GET['group_num']
            sem = request.GET['sem']
            k = file.setTable(group, sem)

        return render(request, 'timetable_gost.html', locals())

# Обработка страницы вывода гостевой версии расписания по преподавателям
def timetable_teachers_gost(request):
    file = ImportJSON()
    if (request.GET):
        teacher = request.GET['teacher']
        sem = request.GET['sem']
        t_list = teacher.split('_')
        str_teacher = ''
        for i in t_list:
            str_teacher += i + " "
        file.SetTableTeacher(teacher, sem)
        k = 1

    return render(request, 'timetable_teachers_gost.html', locals())

# Обработка страницы вывода гостевой версии расписания по аудиториям
def timetable_auds_gost(request):
    file = ImportJSON()
    if (request.GET):
        adress = request.GET['adress']
        cab = request.GET['cab']
        sem = request.GET['sem']
        t_list = adress.split('_')
        str_adress = ''
        for i in t_list:
            str_adress += i + " "
        adress_strk = ""
        for ir in range(0, len(str_adress) - 1):
            adress_strk += str_adress[ir]
            file.SetTableAud(adress_strk, cab, sem)
        k = 1

    return render(request, 'timetable_auds_gost.html', locals())

# Обработка страницы выбора режима вывода расписания
def timetable(request):
    if (request.session.has_key('access')):
        return render(request, 'timetable.html', locals())
    else: return (enter(request))

# Обработка страницы вывода личного кабинета
def options(request):
    import hashlib
    if (request.session.has_key('access')):
        login = request.session['login']
        if (request.session['access'] == "Admin"):
            k=1
            listk = telephoneNumber('Authorisation.json', login, "Admin")
            phone = listk[0]
            FIO = listk[1]

            if (request.GET):
                number = request.GET["number"]
                password = request.GET["password"]
                b = bytes(password, 'utf-8')
                h = hashlib.sha1(b)
                password = h.hexdigest()
                m = SetTelephoneNumber('Authorisation.json', login, "Admin", password, number)

            return render(request, 'options.html', locals())
        elif (request.session['access'] == "Manager"):
            phone = telephoneNumber('Authorisation.json', login, "Manager")[0]
            FIO = telephoneNumber('Authorisation.json', login, "Manager")[1]
            k=0
            login = request.session['login']
            if (request.GET):
                number = request.GET["number"]
                password = request.GET["password"]
                b = bytes(password, 'utf-8')
                h = hashlib.sha1(b)
                password = h.hexdigest()
                m = SetTelephoneNumber('Authorisation.json', login, "Manager", password, number)

            return render(request, 'options.html', locals())
        else: return (enter(request))
    else: return (enter(request))



# Обработка страницы просмотра и редактирования списка пользователей
def users_view(request):
    import hashlib
    if (request.session.has_key('access')):
        login = request.session['login']
        if (request.session['access'] == "Admin"):
            listUsers = getListUsers('Authorisation.json')
            if (request.GET):
                if 'add' in request.GET:
                    access = request.GET["access"]
                    new_login = request.GET["login"]
                    new_password = request.GET["password"]
                    b = bytes(new_password, 'utf-8')
                    h = hashlib.sha1(b)
                    new_password = h.hexdigest()
                    phone = request.GET["phone"]
                    firstname = request.GET["firstname"]
                    middlename = request.GET["middlename"]
                    lastname = request.GET["lastname"]
                    ad_password = request.GET["ad_password"]
                    b = bytes(ad_password, 'utf-8')
                    h = hashlib.sha1(b)
                    ad_password = h.hexdigest()
                    check1 = Add_Users('Authorisation.json', access, new_login, new_password, phone, ad_password, firstname, middlename, lastname, login)
                if 'delete' in request.GET:
                    access_del = request.GET['access_del']
                    login_del = request.GET['login_del']
                    password_del = request.GET['del_password']
                    b = bytes(password_del, 'utf-8')
                    h = hashlib.sha1(b)
                    password_del = h.hexdigest()
                    check2 = DelUser('Authorisation.json', login_del, access_del, login, password_del)

            return render(request, 'Users_view.html', locals())
        else:
            return (enter(request))
    else:
        return (enter(request))

