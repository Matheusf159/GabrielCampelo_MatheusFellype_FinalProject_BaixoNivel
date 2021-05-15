type_r = {"add":"0b100000",
          "sub":"0b100010",
          "and":"0b100100",
          "or" :"0b100101",
          "sll":"0b000000",
          "slr":"0b000010",
          "slt":"0b101010",
          "jr" :"0b001000"}

type_i = {"addi":"0b001000",
          "subi":"",#TO-DO
          "lw"  :"0b100011",
          "lb"  :"0b100000",
          "sb"  :"0b101000",
          "andi":"0b001100",
          "ori" :"0b001101",
          "beq" :"0b000100",
          "bne" :"0b000101",
          "slti":"0b001010"}

type_j = {"j"  :"0b000010",
          "jal":"0b000011"}

registers = {
    "$zero":"0b0",
    
    "$v0"  :"0b10",
    "$v1"  :"0b11",
    
    "$a0"  :"0b100",
    "$a1"  :"0b101",
    "$a2"  :"0b110",
    "$a3"  :"0b111",
    
    "$t0"  :"0b1000",
    "$t1"  :"0b1001",
    "$t2"  :"0b1010",
    "$t3"  :"0b1011",
    "$t4"  :"0b1100",
    "$t5"  :"0b1101",
    "$t6"  :"0b1110",
    "$t7"  :"0b1111",
    
    "$s0"  :"0b10000",
    "$s1"  :"0b10001",
    "$s2"  :"0b10010",
    "$s3"  :"0b10011",
    "$s4"  :"0b10100",
    "$s5"  :"0b10101",
    "$s6"  :"0b10110",
    "$s7"  :"0b10111",
    
    "$t8"  :"0b11000",
    "$t9"  :"0b11001",
    
    '$sp'  :"0b11101",
    
    '$ra'  :"0b11111"}

def substitution(line):
    print("AQUIII: " + line)
    line_split = line.split()
    
    if(line_split[0] in type_r.keys()):
        print("Tipo R")

    elif(line_split[0] in type_i.keys()):
        print("Tipo I")

    elif(line_split[0] in type_j.keys()):
        print("Tipo J")


#instruction[0] in type_r.keys() Idéia para identificação do tipo da operação
file = 'C:/Users/mathe/Documents/GitHub/GabrielCampelo_MatheusFellype_FinalProject_BaixoNivel/input.txt'

with open(file, 'r') as input_file:
    for line in input_file:
        line = line.replace('\n','')
        line = line.replace(',',' ')
        #print(line)
        substitution(line)
    
