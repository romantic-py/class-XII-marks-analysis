file = open('61479.txt','r')

subject = dict()  # subject['subject_code'] = list of tuples (subject_marks_of_student, name_of_student)
subjectName = {'042':'PHYSICS', '043':'CHEMISTRY', '044':'BIOLOGY', '045':'BIOTECHNOLOGY', '301':'ENGLISH', '027':'HISTORY',
               '028': 'POLITICAL SCIENCE', '030':'ECONOMICS', '037':'PSYCHOLOGY', '041':'MATHEMATICS', '083':'COMPUTER SCIENCE',
               '054':'BUSINESS STUDIES', '055':'ACCOUNTANCY', '064':'HOME SCIENCE', '002':'HINDI ELECTIVE',
               '048':'PHYSICAL EDUCATION', '049':'PAINTING', '029':'GEOGRAPHY'
            }

master = []  # list of tuples of the form (average marks, NAME) 
drops = []  # list of students who did not appear for the exam; tuples of the form (ROLL, NAME)

done = False
while not done:
    a = list(map(str, file.readline().split()))
    if len(a) == 0:
        continue
    elif '9717' not in a[0]:
        continue
    for i in range(len(a)):
        if a[i] in ('M','F') and a[i+1].isdigit():
            break
    name = ''
    for j in range(1,i): name += a[j]+' '
    name = name[:-1]
    if a[0] == '9717697': done = True
    j = i+1
    if a[-1] == 'ABST':
        drops.append((a[0], name))
        continue
    elif a[-1] != 'PASS':
        continue
    marks = []
    while j < len(a):
        if not a[j].isdigit():
            break
        if a[j+1].isdigit():
            marks.append(int(a[j+1]))
            if a[j] in subject:
                subject[a[j]].append((int(a[j+1]), name))
            else:
                subject[a[j]] = [(int(a[j+1]), name)]
        j += 3
    assert (len(marks) >= 5)
    if len(marks) > 5:
        marks[4] = max(marks[4:])
    master.append((sum(marks[:5])/5, name))

file.close()
