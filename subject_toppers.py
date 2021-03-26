from mainfile import subject, subjectName

if __name__ == '__main__':
    with open('subject_toppers.txt','w') as out:
        out.write('---SUBJECT TOPPERS---\n\n')
        for a in subject.keys():
            print('SUBJECT:', a)
            out.write('SUBJECT: {}, '.format(subjectName[a]))
            red = subject[a]
            red.sort(reverse=False)
            out.write('HIGHEST: {}\n'.format(red[-1][0]))
            for i in range(len(red)):
                if red[i][0] == red[-1][0]:
                    out.write('{}\n'.format(red[i][1]))
            out.write('\n')
