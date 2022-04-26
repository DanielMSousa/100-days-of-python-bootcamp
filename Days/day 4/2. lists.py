#lists
#lists start with "[" and "]" and have its items separated by ","

states_of_america = ["Delaware", "Pennysylvania"]

#The first item starts with 0
print(states_of_america[0])

print(states_of_america[1])

#using negatives number starts counting from the ending of the list
print(states_of_america[-1])

#You can change the elements of the list

states_of_america[1] = "Pencilvania"
print(states_of_america)

states_of_america.append("Angelaland")

print(states_of_america)

states_of_america.extend(['Angelalalaland', 'Jack Bauer Land'])

print(states_of_america)