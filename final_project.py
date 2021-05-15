type_r = {"add":["100000","AL"],
          "sub":["100010","AL"],
          "and":["100100","AL"],
          "or" :["100101","AL"],
          "sll":["000000", "S"],
          "slr":["000010", "S"],
          "slt":["101010","AL"],
          "jr" :["001000","JR"]}

type_i = {"addi":["001000","AL"],
          "subi":["",""],#TO-DO
          "lw"  :["100011","LS"],
          "lb"  :["100000","LS"],
          "sb"  :["101000","LS"],
          "andi":["001100","AL"],
          "ori" :["001101","AL"],
          "beq" :["000100","B"],
          "bne" :["000101","B"],
          "slti":["001010","AL"]}

type_j = {"j"  :"000010",
          "jal":"000011"}

registers = {
    "$zero":"00000",
    
    "$v0"  :"00010",
    "$v1"  :"00011",
    
    "$a0"  :"00100",
    "$a1"  :"00101",
    "$a2"  :"00110",
    "$a3"  :"00111",
    
    "$t0"  :"01000",
    "$t1"  :"01001",
    "$t2"  :"01010",
    "$t3"  :"01011",
    "$t4"  :"01100",
    "$t5"  :"01101",
    "$t6"  :"01110",
    "$t7"  :"01111",
    
    "$s0"  :"10000",
    "$s1"  :"10001",
    "$s2"  :"10010",
    "$s3"  :"10011",
    "$s4"  :"10100",
    "$s5"  :"10101",
    "$s6"  :"10110",
    "$s7"  :"10111",
    
    "$t8"  :"11000",
    "$t9"  :"11001",
    
    '$sp'  :"11101",
    
    '$ra'  :"11111"}

def substitution(line):
    print("AQUIII: " + line)
    line_split = line.split()
    
    
    if(line_split[0] in type_r.keys()):
        print("Tipo R")
        op_func = type_r[line_split[0]]
        #if(type_r[line_split[0]][1]) == "AL"):
            
    elif(line_split[0] in type_i.keys()):
        print("Tipo I")
        op_func = type_i[line_split[0]]
        if(op_func[1] == "AL"):
            inst =  op_func[0] + registers[line_split[2]] + registers[line_split[1]] + '{0:016b}'.format(int(line_split[3]))
            print(hex(int(inst,2)))

    elif(line_split[0] in type_j.keys()):
        print("Tipo J")
        op_func = type_j[line_split[0]]


#instruction[0] in type_r.keys() Idéia para identificação do tipo da operação
#file = 'C:/Users/mathe/Documents/GitHub/GabrielCampelo_MatheusFellype_FinalProject_BaixoNivel/input.txt'
file = './input.txt'

with open(file, 'r') as input_file:
    for line in input_file:
        line = line.replace('\n','')
        line = line.replace(',',' ')
        #print(line)
        substitution(line)
        break
    
