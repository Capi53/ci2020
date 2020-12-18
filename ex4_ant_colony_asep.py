import random

def generate_trail_phelomone_probalbility(cell):
    """
    道標フェロモンを作る関数．'10'の数の分だけランダムに0~1の値を出力する．

    Parameters
    ---------
    cell : string 
        セル

    Returns
    -------
    trail_phelomone_p : list
        フェロモンが存在する確率
    """
    num = cell.count('10')-1 if cell[:-2] == "10" else cell.count('10')
    if num != 0:
        trail_phelomone_p = [random.uniform(0,1) for _ in range(num)]
        trail_phelomone_p.append(trail_phelomone_p[0])
    else :
        trail_phelomone_p = []
    return trail_phelomone_p


def next_cell(cell, phel):
    """
    時刻tのセルにおいて'10'を見つけて，0に道標フェロモンがあった場合，'01'に置き換える．

    Parameters
    ---------
    cell : string 
        セル
    phel : string
        フェロモン

    Returns
    -------
    cell : striing
        時刻t+1のセル
    """
    cell = cell[-1] + cell + cell[0]
    phel = phel[-1] + phel + phel[0]
    p = generate_trail_phelomone_probalbility(cell)
    cell_l = cell.split("10")
    result = ''
    if len(cell_l)>=2:
        for i in range(len(p)-1):
            if phel[len(cell_l[0])] == '1':
                probability = 0.75
            else:
                probability = 0.25
            tmp_l = [cell_l[0]] +[cell_l[1]]
            # print("tmp1:",tmp_l)
            # print("cell1:    ",cell_l)
            del cell_l[1]
            # print("tmp2:",tmp_l)
            
            if p[i] <= probability:
                cell_l[0] = '01'.join(tmp_l)
            else:
                cell_l[0] = '10'.join(tmp_l)
            # print("cell2:    ",cell_l)
            result = cell_l[0]
    else:
        result = cell
    # print("======="*3)
    # print("cell:\t", cell[1:-1])
    # print(cell == phel)
    phel = ''.join([str(random.randint(0,1)) if i == '1' else '0' for i in phel])[1:-1]
    # print("phel:\t",phel)
    phel = ''.join([max(i) for i in zip(phel, cell[1:-1])])
    # print("phel:\t",phel)
    cell = result[1:-1]
    return cell, phel

def main():
    #課題1
    #felomoneがあったら75%,なかったら25%
    #felomoneがあるところは毎回50%で蒸発する．    
    init_cell_1 = "111100011001111100110101"
    init_phel_1 = init_cell_1
    init_cell_2 = "011111111001100000110000"
    init_phel_2 = init_cell_2

    print(init_cell_1)

    cell = init_cell_1
    phel = init_phel_1
    for _ in range(100):
        cell, phel = next_cell(cell,phel)
    print(cell)
    cell = init_cell_2
    phel = init_phel_2       
    # for _ in range(100):
    #     cell, phel = next_cell(cell, phel)
    # print(cell)  

if __name__ == "__main__":
    main()