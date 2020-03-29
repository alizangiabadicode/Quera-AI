def process(path):
    #some code 
    athletes = []
    normal_people = []
    content = ""
    with open(path, 'r') as file:
        content = file.read().split('\n')
        for c in content:
            height, weight, athlete_or_normal = c.split(' ')[:3]
            print(height,weight,athlete_or_normal)
            height2 = float(height)
            weight2 = float(weight)
            bmi = weight2/( height2 / 100) ** 2
            if athlete_or_normal == "ATHLETE" :
                athletes.append((int(height), weight2, bmi)) 
            else:
                normal_people.append((int(height), weight2, bmi))
    athletes_average_bmi = normal_average_bmi = 0
    for a in athletes:
        athletes_average_bmi += a[2]
    if len(athletes) > 0:
        # print(athletes_average_bmi, len(athletes), athletes_average_bmi / len(athletes))
        athletes_average_bmi = athletes_average_bmi / len(athletes)
    for n in normal_people:
        normal_average_bmi += n[2]
    if len(normal_people) > 0:
        normal_average_bmi /= len(normal_people)
    return athletes , athletes_average_bmi , normal_people, normal_average_bmi