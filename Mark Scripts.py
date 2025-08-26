#A program that can mark Multipe-Choice questions
def mark():
    
#The marking scheme
    m_sch = input('The marking scheme?: ')
    
#The student's response
    ans = input("The student's response: ")
    
#Marks count
    corrects = 0
    wrongs = 0
    
#Filling in for unanswered questions    
    if len(m_sch) > len(ans):
        d = len(m_sch) - len(ans)
    else:
        d = 0
    ans_l =  [h for h in ans]
    for r in range(d):
        ans_l.append('NA')
        
# 3 years later, I look at the code and I see that the above paragraph could have been just:
# ans_l += ['NA' for i in range(max(len(m_sch)-len(ans), 0))] # (untested)

    
#Results
    results = []
        

#Scan through and mark the script        
    for i in range(len(m_sch)):
        if m_sch[i] == ans_l[i]:
            results.append(f'{i+1}.{ans_l[i]} Correct')
            corrects += 1
            
        elif ans_l[i] == 'NA':
            results.append(f'{i+1}.Not answered; {m_sch[i]}')
            
        
        else:
            results.append(f'{i+1}.{ans_l[i]} X {m_sch[i]}')
            wrongs += 1
#Score and display results
    percent_score = corrects*100/len(m_sch)
    print(f'\nTotal number of questions: {len(m_sch)}\nCorrectly answered: {corrects}\nIncorrectly answered: {wrongs}\nUnanswered = {d}\nScore: {percent_score}%')

#To review your answers    
    view = input('View results?(y/n): ')
    if view == 'y':
        for rr in results:
            print(rr)
