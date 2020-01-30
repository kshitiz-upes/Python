score_sheet = []
mark_sheet = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    score_sheet.append(score)
    mark_sheet.append([name, score])
a = sorted(list(set(score_sheet)))[1]
for name,score in sorted(mark_sheet):
        if score == a:
                print(name)
             
             


      
   

