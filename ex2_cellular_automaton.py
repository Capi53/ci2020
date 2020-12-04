import random 

def next_cell(cell):
    if cell[0] == "0" and cell[-1] == "1":
        cell = cell[1:len(cell)-1].replace('10', '01')
        cell = "1" + cell + "0" 
    else:
        cell = cell.replace('10', '01')
    return cell

def get_displacement(cell, t):
    while t >= 1:
        cell = next_cell(cell)
        # print(cell)
        t -= 1
    return cell

def list_to_str(l):
    return ''.join(l)

def bin_to_dec(binary_str):
    return int(binary_str, 2)

def cell_generator(num):
    cell = [random.randint(0,1) for _ in range(num)]
    print(cell)
    return ''.join(cell)

def main():
    cell = cell_generator(100) #100マス
    print("--"*10+"input"+"--"*10)
    print("init cell : ", cell)
    print("--"*10+"output"+"--"*10)
    out_cell = get_displacement(cell, 100)
    print("decimal : ",bin_to_dec(out_cell))
    print("binary : ", out_cell) 

if __name__ == "__main__":
    main()