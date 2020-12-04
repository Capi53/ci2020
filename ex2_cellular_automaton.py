def next_cell(cell):
    if cell[0] == "0" and cell[-1] == "1":
        cell = cell[1:len(cell)-1].replace('10', '01')
        cell = "1" + cell + "0" 
    else:
        cell = cell.replace('10', '01')
    return cell

def get_displacement(cell, t):
    if type(cell) == list:
        cell = list_to_str(cell)
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

def main():
    print("--"*10+"問題1"+"--"*10)
    print("init cell : 111100011001111100110101")
    cell1 = "111100011001111100110101"
    print("--"*10+"答え"+"--"*10)
    bs1 = get_displacement(cell1, 100)
    print("10進数 : ",bin_to_dec(bs1))
    print("2進数 : ",bs1) 

    print("--"*10+"問題2"+"--"*10)
    print("init cell : 011111111001100000110000")
    cell2 = "011111111001100000110000"
    print("--"*10+"答え"+"--"*10)
    bs2 = get_displacement(cell2, 100)
    print("10進数 : ",bin_to_dec(bs2))
    print("2進数 : ",bs2) 

if __name__ == "__main__":
    main()