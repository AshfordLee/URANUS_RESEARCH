import pandas as pd


def get_matrix(n):
    matrix=[]#list中嵌套list来表达矩阵
    for i in range(n):
        matrix.append([0]*n)

    num=1#从1填充到n^2
    row=0
    column=0
    #从(0,0)开始填充，逆时针螺旋

    
    direction=0#初始方向为向下

    top=0
    bot=n-1
    left=0
    right=n-1
    #四个初始边界，撞到了边界代表着要改变方向了

    while num<=n*n:
        matrix[row][column]=num


        if direction==0:
            #往下走
            if row<bot:
                #距离下边界至少一格距离
                row=row+1

            else:
                #已经撞到了下边界
                direction=1
                column=column+1
                left=left+1
                #改变方向，调整列来向右走，左边界向右移动一格

        elif direction==1:
            #往右走

            if column<right:
                #距离右边至少一个距离
                column=column+1

            else:
                #撞到了右边
                direction=2
                row=row-1
                bot=bot-1
                #改变方向，调整行来向右走，下边界向上移动一格

        elif direction==2:
            #向上走

            if row>top:
                #距离上面至少一格距离
                row=row-1

            else:
                #撞到了上面
                direction=3
                column=column-1
                right=right-1
                #改变方向，调整列来向左走，右边界向左移动一格

        elif direction==3:
            #向左走

            if column>left:
                #距离左边至少一个格子
                column=column-1

            else:
                #撞到了左边
                direction=0
                row=row+1
                top=top+1

        num=num+1


    ans=pd.DataFrame(matrix)
    return ans


if __name__=="__main__":
    n=int(input("输入n"))
    ans=get_matrix(n)
    print("输出矩阵：")
    print(ans)
