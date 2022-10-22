with open("paragliding-sub3-attempt3.txt") as txt :
    lignes = txt.read().splitlines()
nombre_lignes = len(lignes)-1
lignes.pop(0)

open('answers.txt', 'w').close()

def check_space(string) :
    for x in string :
        if x == " " :
            return False
    return True

def disassemble_string(string) :
    temporary = ""
    ListOfNumbers = []
    for x in string :
        if x != " " : 
            temporary += str(x)
        else :
            ListOfNumbers.append(int(temporary))
            temporary = ""
    ListOfNumbers.append(int(temporary))
    return ListOfNumbers


heights = []
lengths =[]
distances = []
counter = -1
for x in lignes :
    if check_space(x) == True :
        NextCountNumber = 2
        counter += 1
        continue
    elif NextCountNumber == 2 :
        lengths = disassemble_string(x)
        NextCountNumber -= 1
    elif NextCountNumber == 1 :
        heights = disassemble_string(x)
        comparison = 0
        distances = []
        for x in range(len(heights)) :
            y = x
            z = x
            while lengths[y] != lengths[0] :
                if heights[y] < heights[y-1] : 
                    break
                y -= 1
            while lengths[z] != lengths[len(lengths)-1] :
                if heights[z] < heights[z+1] : 
                    break
                z += 1
            if abs(lengths[x] -lengths[z]) > abs(lengths[x] -lengths[y]) :
                distances.append(str(abs(lengths[x] - lengths[z])))
            else : 
                distances.append(str(abs(lengths[x] - lengths[y])))
        distances = " ".join(distances)
        with open('answers.txt', 'a') as answers:
            answers.write(f"Case #{str(counter)}: {distances}")
            answers.write("\n")
        distances = []
txt.close()