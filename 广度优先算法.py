import time as tm
g_dict_layouts = {}
#每个位置可交换的位置集合
g_dict_shifts = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5],
                 3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
                 6:[3,7],  7:[4,6,8], 8:[5,7]}

def swap_chr(a, i, j):
    if i > j:
        i, j = j, i
    #得到ij交换后的数组
    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
    return b

def solvePuzzle_depth(srcLayout, destLayout):
    #先进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
    #这是判断起始状态是否能够到达目标状态，同奇同偶时才是可达
    src=0;dest=0
    for i in range(1,9):
        fist=0
        for j in range(0,i):
          if srcLayout[j]>srcLayout[i] and srcLayout[i]!='0':#0是false,'0'才是数字
              fist=fist+1
        src=src+fist

    for i in range(1,9):
        fist=0
        for j in range(0,i):
          if destLayout[j]>destLayout[i] and destLayout[i]!='0':
              fist=fist+1
        dest=dest+fist
    if (src%2)!=(dest%2):#一个奇数一个偶数，不可达
        return -1, None

	#初始化字典
    g_dict_layouts[srcLayout] = -1
    stack_layouts = []
    stack_layouts.append(srcLayout)#当前状态存入列表

    bFound = False
    while len(stack_layouts) > 0:
        curLayout = stack_layouts.pop(0)#出栈
        if curLayout == destLayout:#判断当前状态是否为目标状态
            break

        # 寻找0 的位置。
        ind_slide = curLayout.index("0")
        lst_shifts = g_dict_shifts[ind_slide]#当前可进行交换的位置集合
        for nShift in lst_shifts:
            newLayout = swap_chr(curLayout, nShift, ind_slide)

            if g_dict_layouts.get(newLayout) == None:#判断交换后的状态是否已经查询过
                g_dict_layouts[newLayout] = curLayout
                stack_layouts.append(newLayout)#存入集合

    lst_steps = []
    lst_steps.append(curLayout)
    while g_dict_layouts[curLayout] != -1:#存入路径
        curLayout = g_dict_layouts[curLayout]
        lst_steps.append(curLayout)
    lst_steps.reverse()
    return 0, lst_steps


if __name__ == "__main__":
	#测试数据输入格式
    srcLayout  = "283104765"
    destLayout = "123804765"

    retCode, lst_steps = solvePuzzle_depth(srcLayout, destLayout)
    if retCode != 0:
        print("目标布局不可达")
    else:
        for nIndex in range(len(lst_steps)):
            print("step #" + str(nIndex + 1))
            print(lst_steps[nIndex][:3])
            print(lst_steps[nIndex][3:6])
            print(lst_steps[nIndex][6:])

