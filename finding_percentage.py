i=0
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
query_scores = student_marks[query_name]
total_scores = sum(query_scores)
avg = float(total_scores/len(query_scores))
print("%.2f" %avg)

