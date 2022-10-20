with open("test.txt") as txt :
    lignes = txt.read().splitlines()
nombre_lignes = lignes[0]*3
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
        default = lengths[0]
        distances = []
        for x in range(len(heights)-1) :
            if x == 0 or x == len(heights)-1 :
                distances.append("0")
                continue
            if heights[x-1] > heights[x] :
                default = lengths[x-1]
            distances.append(str(lengths[x]-default))
        distances.append("0")
        distances = " ".join(distances)
        with open('answers.txt', 'a') as answers:
            answers.write(f"Case #{str(counter)}: {distances}")
            answers.write("\n")
        distances = []






        

    
        








txt.close()