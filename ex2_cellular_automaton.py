import random 
import matplotlib.pyplot as plt 

def next_cell(cell):
    cell = cell[-1] + cell + cell[0]
    cell = cell.replace('10', '01')
    cell = cell[1:-1]

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

def get_flow_rate(cell, loops, target):
    """
    流量を調べる関数

    Parameters
    ---------
    cell  string 
        セル
    loops : int
        ループ回数
    target : int
        ターゲットとするindexの番号

    Returns
    -------
    f_rate_counter : int
        流量(0 <=x<= loops)
    """
    tmp_cell = cell #比較対象
    f_rate_counter = 0 #ますで変化があった回数

    while loops >= 1:
        cell = next_cell(cell)
        if cell[target] != tmp_cell[target]:
            f_rate_counter += 1
        tmp_cell = cell
        loops -= 1
    return f_rate_counter//2

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
    # for i in range(1,52):
    #     input_cell = cell_generator(100, i)
    #     # print(input_cell)
    #     if not is_cluster(input_cell):
    #         out_cell = get_displacement(input_cell, 10)#だいたい10回やればクラスタができるかどうか分かるはずだ!!
    #         if is_cluster(out_cell):
    #             print(out_cell)
    #             print("Cluster found")
    #             print(i)
    #             exit()
    #         else:
    #             print("Cluster not found")
    #     else :
    #         print(input_cell)
    #         print("Cluster found")
    #         print(i)
    #         exit()

    #--rep3--
    #流量を求めて配列に保存する．
    flows = [0]
    for i in range(1, 101):
        input_cell = cell_generator(100,i)
        flows.append(get_flow_rate(input_cell,100,1))#100ますのセルを100回動かすのでtargetもランダムで選んでもいいかも
    x=[int(idx) for idx in range(101)]
    plt.figure(0,(6,4))
    plt.plot(x, flows,linestyle="solid", marker="o")
    plt.xlabel("cells")
    plt.ylabel("flows")
    plt.savefig("任意のセルでの流量観測")



if __name__ == "__main__":
    main()