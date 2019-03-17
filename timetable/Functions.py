# Функция добавления группы в базу данных расписания
def WriteGroup(file, **info):
    import json

    myfile = open (file,mode='r', encoding='UTF-8')
    data = json.load(myfile)
    myfile.close()
    myfile = open (file,mode='w', encoding='UTF-8')
    j=0
    for i in data:
        if info['group'] == i['group']:
            j += 1
        else:
            continue
    if j==0:
        data.append(info)
        k=1
    else: k=0
    json.dump(data, myfile, indent=4, sort_keys=True, ensure_ascii=False)
    myfile.close()
    return k

# Функция смены пароля в базе данных авторизации
def SetPassword(old, new, login, access):
    import json

    myfile = open('Authorisation.json', mode='r', encoding='UTF-8')
    data = json.load(myfile)
    data1 = data['access']
    i1 = 0
    k=0
    i2 = 0
    if access == "Manager":
        for i in data1['manager']:
            if ((i['login'] == login) & (i['password'] == old)):
                data['access']['manager'][i1]['password']=new
                k=1
                break
        i1+=1
    elif access == "Admin":
        for i in data1['administrator']:
            if ((i['login'] == login) & (i['password'] == old)):
                data['access']['administrator'][i2]['password']=new
                k =1
                break
        i2+=1
    print(data)
    myfile2 = open('Authorisation.json', mode='w', encoding='UTF-8')
    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
    myfile2.close()
    return  k

# Функция добавления занятия
def WriteDay(file, group, **info):
    import json

    myfile = open(file, mode='r', encoding='UTF-8')
    data = json.load(myfile)
    myfile.close()
    myfile2 = open(file, mode='w', encoding='UTF-8')
    k=0
    for i in data:
        if (i['group'] == group):
            if 'week' in i:
                for j in i['week']:
                    if ((j['day'] == info['day']) & (j['chet'] == info['chet']) & (j['time'] == info['time'])& (j['sem'] == info['sem'])):
                        k+=1
                        break
                if k==0:
                    i['week'].append(info)
            else:
                if k==0:
                    i['week'] = []
                    i['week'].append(info)

    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
    myfile2.close()
    if (k>0): return 0
    else: return 1


#функция проверки аккаунта
def CheckAcc(file, login, password):
    import json

    myfile = open(file, mode='r', encoding='UTF-8')
    data = json.load(myfile)

    data = data['access']
    k='None'
    manager = data['manager']
    for i in manager:
        if ((i['login']==login)&(i['password']==password)): k='Manager'
    admin = data['administrator']
    for i in admin:
        if ((i['login'] == login) & (i['password'] == password)): k = 'Admin'

    return k

# Получение значения номера телефона
def telephoneNumber(file, login, access):
    import json
    phone = 0
    FIO = ""
    myfile = open(file, mode='r', encoding='UTF-8')
    data = json.load(myfile)
    data1 = data['access']
    i1 = 0
    i2 = 0
    if access == "Manager":
        for i in data1['manager']:
            if ((i['login'] == login)):
                phone = data['access']['manager'][i1]['phone']
                firstname = data['access']['manager'][i1]['firstname']
                lastname = data['access']['manager'][i1]['lastname']
                middlename = data['access']['manager'][i1]['middlename']
                FIO = lastname+" "+firstname+" "+middlename
                break
        i1 += 1
    elif access == "Admin":
        for i in data1['administrator']:
            if ((i['login'] == login)):
                phone = data['access']['administrator'][i2]['phone']
                firstname = data['access']['administrator'][i2]['firstname']
                lastname = data['access']['administrator'][i2]['lastname']
                middlename = data['access']['administrator'][i2]['middlename']
                FIO = lastname + " " + firstname + " " + middlename
                break
        i2 += 1
    ret = []
    ret.append(phone)
    ret.append(FIO)
    return ret

# Смена телефонного номера
def SetTelephoneNumber(file, login, access, password, phone):
    import json

    myfile = open(file, mode='r', encoding='UTF-8')
    data = json.load(myfile)
    data1 = data['access']
    i1 = 0
    k = 0
    i2 = 0
    if access == "Manager":
        for i in data1['manager']:
            if ((i['login'] == login) & (i['password'] == password)):
                data['access']['manager'][i1]['phone'] = phone
                k = 1
                break
        i1 += 1
    elif access == "Admin":
        for i in data1['administrator']:
            if ((i['login'] == login) & (i['password'] == password)):
                data['access']['administrator'][i2]['phone'] = phone
                k = 1
                break
        i2 += 1
    print(data)
    myfile2 = open(file, mode='w', encoding='UTF-8')
    json.dump(data, myfile2, indent=4, sort_keys=True, ensure_ascii=False)
    myfile2.close()
    return k

# Функция получения списка пользователей
def getListUsers(file):
    import json

    myfile = open(file, mode='r', encoding='UTF-8')
    data = json.load(myfile)
    data1 = data['access']
    listUsers = []
    listUsers_admin = []
    listUsers_manager = []
    i1 = 0
    k=0
    i2 = 0

    for i in data1['administrator']:
        listUsers_admin.append(i)
    for i in data1['manager']:
        listUsers_manager.append(i)
    listUsers.append(listUsers_admin)
    listUsers.append(listUsers_manager)
    return  listUsers

# Функция добавления пользователя
def Add_Users(file, access, login, password, phone, ad_password, firstname, middlename, lastname, ad_login):
    import json
    user = {'login': login, 'password': password, 'phone': phone, 'firstname': firstname, 'middlename': middlename, 'lastname':lastname}
    myfile = open(file, mode='r', encoding='UTF-8')
    data_need = json.load(myfile)
    data = data_need['access']
    myfile.close()
    check = 1

    temp = 0

    admin = data['administrator']
    for i in admin:
        if ((i['login'] == ad_login) & (i['password'] == ad_password)):
            temp = 1
    if temp == 0:
        check = 3
        return check
    else:
        data_managers = data['manager']
        data_administrators = data['administrator']
        for i in data_managers:
            if i['login'] == login:
                check = 0
        for i in data_administrators:
            if i['login'] == login:
                check = 0
        if check == 1:
            myfile = open(file, mode='w', encoding='UTF-8')
            if access == "manager":
                data_need['access']['manager'].append(user)
            if access == "administrator":
                data_need['access']['administrator'].append(user)
            json.dump(data_need, myfile, indent=4, sort_keys=True, ensure_ascii=False)
            myfile.close()
            return (check)
        else: return(check)

# Функция удаления пользователя
def DelUser(file, login, access, ad_login, ad_password):
    import json

    myfile = open(file, mode='r', encoding='UTF-8')
    data_need = json.load(myfile)
    data = data_need['access']
    myfile.close()
    check = 0
    data_managers = data['manager']
    data_administrators = data['administrator']
    temp = 0
    admin = data['administrator']
    if login == ad_login: return 5
    else:
        for i in admin:
            print(i['login'])
            print(ad_login)
            print(i['password'])
            print(ad_password)
            if ((i['login'] == ad_login) & (i['password'] == ad_password)):
                print('ПАДАШЕЛ', i['login'], ad_login, i['password'], ad_password)
                temp = 1
        if temp == 0:
            check = 3
            return check
        else:
            if access == "manager":
                for i in data_managers:
                    if i['login'] == login: check = 1
            if access == "administrator":
                for i in data_administrators:
                    if i['login'] == login: check = 1

            if check == 1:
                if access == "manager":
                    temp = 0
                    for i in data_need['access']['manager']:
                        if i['login'] == login:
                            del data_need['access']['manager'][temp]
                        temp += 1

                elif access == "administrator":
                    temp = 0
                    for i in data_need['access']['administrator']:
                        if i['login'] == login:
                            del data_need['access']['administrator'][temp]
                        temp += 1

                myfile = open('Authorisation.json', mode='w', encoding='UTF-8')
                json.dump(data_need, myfile, indent=4, sort_keys=True, ensure_ascii=False)
                myfile.close()
                return check
            else: return check


