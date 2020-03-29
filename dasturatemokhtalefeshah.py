# dasturat = [
#     ['food-water-.5', 'food-dinner-1.0'],
#     ['promote-judge-50', 'promote-minister-80', 'promote-governer-100'],
#     ['travel-ground-45', 'travel-sea-58']
# ]

dasturat = {
    'food': ['water-.5', 'dinner-1.0'],
    'promote': ['judge-50', 'minister-80', 'governer-100'],
    'travel': ['ground-45', 'sea-58']
}

input = input().split()
found = False
if dasturat.get(input[0]):
    for item in dasturat.get(input[0]):
         if item.split('-')[0] == input[1]:
             print(float(item.split('-')[1]))
else:
    print(float(10))
# for d in dasturat:
#     if (d[0].split("-")[0] == dastur[0]):
#         for dd in d:
#             temp_split = dd.split('-')
#             if (temp_split[1] == dastur[1]):
#                 print(float(temp_split[2]))
#                 found = True
#                 break
#         if (not found):
#             found =True
#     if (found):
#         break
# if (not found):
    