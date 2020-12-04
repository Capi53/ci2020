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

def cell_generator(size, sum_=0):
    if sum_ == 0:
        cell = [str(random.randint(0,1)) for _ in range(size)]
    else:
        cell = [str(0) for _ in range(size)]
        idx = random.sample([int(idx) for idx in range(0,size)], sum_)
        for i in idx:
            cell[i] = "1"
    return ''.join(cell)

def is_cluster(cell):
    #クラスターは粒子が2つ以上連なった状態
    if '11' in cell:
        return True
    else:
        return False

def main():
    #--rep1--
    # cell = cell_generator(100) #100マス
    # print("--"*10+"input"+"--"*10)
    # print("init cell : ", cell)
    # print("--"*10+"output"+"--"*10)
    # out_cell = get_displacement(cell, 100)
    # print("decimal : ",bin_to_dec(out_cell))
    # print("binary : ", out_cell) 

    #--rep2--
    for i in range(1,52):
        input_cell = cell_generator(100, i)
        # print(input_cell)
        if not is_cluster(input_cell):
            out_cell = get_displacement(input_cell, 10)#だいたい10回やればクラスタができるかどうか分かるはずだ!!
            if is_cluster(out_cell):
                print(out_cell)
                print("Cluster found")
                print(i)
                exit()
            else:
                print("Cluster not found")
        else :
            print(input_cell)
            print("Cluster found")
            print(i)
            exit()


if __name__ == "__main__":
    main()