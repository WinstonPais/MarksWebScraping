def getNameUsn(fullString):
    retusn=[]
    retname=[]
    for student in fullString.strip().split('-------------------------------------------------------------------'):
        if student.strip().startswith('no data available'):
            continue
        lst=student.strip().split('\n')
        if lst == ['']:
            continue
        usn,name=lst[0].split()[-1]," ".join(lst[0].split()[:-1])
        retusn.append(usn)
        retname.append(name)
    return retusn,retname

def getdata(fullString):
    studentdataList=[]
    for student in fullString.strip().split('-------------------------------------------------------------------'):
        # print(student)
        if student.strip().startswith('no data available'):
            continue
        lst=student.strip().split('\n')
        stud=[]
        for i in range(len(lst)-3):
            index=i+2
            subject=lst[index]
            temp_subSplit=subject.split()
            subLst=[]
            subLst.append(temp_subSplit[0])
            subLst.append(" ".join(temp_subSplit[1:-7]))
            for colVals in range(len(temp_subSplit)-7,len(temp_subSplit)):
                subLst.append(temp_subSplit[colVals])
            stud.append(subLst)
        studentdataList.append(stud)
    return studentdataList

    #     if lst == ['']:
    #         continue
    #     studentData = lst[1][69:]
    #     print(studentData)
    #     import re
    #     matches = re.finditer(' P|\D F',studentData)
    #     matches_positions = [match.start() for match in matches]
    #     print(matches_positions)
    #     prev=0
    #     stud=[]
    #     for i in matches_positions:
    #         subject=studentData[prev:i+3].strip()
    #         prev=i+3
    #         temp_subSplit=subject.split()
    #         subLst=[]
    #         subLst.append(temp_subSplit[0])
    #         subLst.append(" ".join(temp_subSplit[1:-7]))
    #         for colVals in range(len(temp_subSplit)-7,len(temp_subSplit)):
    #             subLst.append(temp_subSplit[colVals])
    #         stud.append(subLst)
    #     studentdataList.append(stud)
    # return studentdataList
