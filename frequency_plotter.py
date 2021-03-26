import matplotlib.pyplot as plt
from mainfile import subject, subjectName

if __name__ == "__main__":
    code = input('ENTER SUBJECT CODE: ')
    if code not in subject: 
        code = '301'

    red = subject[code]
    fig = plt.figure()

    X = list(range(100+1))
    Y = [0 for i in range(100+1)]

    for a in red: Y[a[0]] += 1

    plt.bar(X, Y)
    plt.ylabel('Frequency')
    plt.title('Frequency of marks ({}) - no. of students:{}'.format(subjectName[code], len(red)))
    plt.xlabel('MARKS')
    plt.show()