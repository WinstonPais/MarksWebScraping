def getNameUsn(fullString):
    for student in fullString.strip().split('-------------------------------------------------------------------'):
        if student.strip().startswith('no data available'):
            continue
        lst=student.strip().split('\n')
        if lst == ['']:
            continue
        usn,name=lst[0].split()[-1]," ".join(lst[0].split()[:-1])
        return usn,name
