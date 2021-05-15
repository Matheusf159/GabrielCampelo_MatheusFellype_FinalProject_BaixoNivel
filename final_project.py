import re

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
          "sw"  :["101011","LS"],
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

labels = {}

line_n = 0x00400024

def complemento2(value):
    value = '{0:016b}'.format(int(value)*-1)
    new = ''
    for i in value:
        if(i == '0'):
            new += '1'
        else:
            new += '0'
    soma = int(new,2)+1
    return soma

def substitution(line):
    line_split = line.split()
    print(line_split)
    if(line_split[0] in type_r.keys()):
        print("Tipo R")
        op_func = type_r[line_split[0]]

        if(op_func[1] == "AL"):
            inst = "000000" + registers[line_split[2]] + registers[line_split[3]] + registers[line_split[1]] + "00000" + op_func[0]

        elif(op_func[1] == "S"):
            inst = "000000" + "000000" + registers[line_split[2]] + registers[line_split[1]] + "00100" + op_func[0]
            
        elif(op_func[1] == "JR"):
            inst = "000000" + registers[line_split[1]] + "00000" + "00000" + "00000" + op_func[0]
            
        print(hex(int(inst,2)))
        saida.append(hex(int(inst,2)))
                     
    elif(line_split[0] in type_i.keys()):
        
        print("Tipo I")
        op_func = type_i[line_split[0]]
        
        if(op_func[1] == "AL"):
            if int(line_split[3]) < 0:
                line_split[3] = complemento2(line_split[3])
                
            inst =  op_func[0] + registers[line_split[2]] + registers[line_split[1]] + '{0:016b}'.format(int(line_split[3]))
            print(hex(int(inst,2)))
            saida.append(hex(int(inst,2)))
            
        elif(op_func[1] == "LS"):
            i,s,_ = re.split('[()]',line_split[-1])
            if int(i) < 0:
                i = complemento2(i)
            inst =  op_func[0] + registers[s] + registers[line_split[1]] + '{0:016b}'.format(int(i))
            print(hex(int(inst,2)))
            saida.append(hex(int(inst,2)))
            
        elif(op_func[1] == "B"):
            #label = labels[op_func-1]
            #if int(line_split[3]) < 0:
            #    line_split[3] = complemento2(line_split[3])
            #inst =  op_func[0] + registers[line_split[1]] + registers[line_split[2]] #+ '{0:016b}'.format(int(i))
            #print(hex(int(inst,2)))
            print('nop')
        #print(hex(int(inst,2)))

    elif(line_split[0] in type_j.keys()):
        print("Tipo J")
        op_func = type_j[line_split[0]]
        inst = op_func + '{0:016b}'.format(int(labels[line_split[-1]]*4))
        print(hex(int(inst,2)))
        saida.append(hex(int(inst,2)))

#file = 'C:/Users/mathe/Documents/GitHub/GabrielCampelo_MatheusFellype_FinalProject_BaixoNivel/input.txt'
file = './input.txt'
arquivo = './output.txt'
#arquivo = 'C:/Users/mathe/Documents/GitHub/GabrielCampelo_MatheusFellype_FinalProject_BaixoNivel/output.txt'

saida = []

with open(file, 'r') as input_file:
    for line in input_file:
        line = line.replace('\n','')
        line = line.replace(',',' ')
        valid = re.search('[\w]*[:\s*]$',line)
        
        if ((type(valid)) == re.Match):
            lb = line.replace(':','')
            labels[lb] = line_n
        line_n += 4

with open(file, 'r') as input_file:
    line_n = 0x00400024
    for line in input_file:
        line = line.replace('\n','')
        line = line.replace(',',' ')
        substitution(line)
        line_n += 4
        

print("SAIDA FINAL", saida)

output_file = open(arquivo, "w+")

for out in saida:
    output_file.writelines(out + '\n')

output_file.close()

