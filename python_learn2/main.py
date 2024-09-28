#函数的定义与使用

#1.函数的定义格式
""""
def 函数名(参数)：
    函数内容
"""
# def Get_max(a,b):
#     if a>=b:
#         print(f"最大的数为{a}")
#     else :
#         print(f"最大的数为{b}")
# a = int(input())
# b = int(input())
# Get_max(a,b)

#函数的注释
# def Get_max(a,b):
#     """
#     比较两数的大小
#     :param a: 参数1
#     :param b: 参数2
#     :return: 返回值
#     """
#     if a>=b:
#         print(f"最大的数为{a}")
#     else :
#         print(f"最大的数为{b}")
# a = int(input())
# b = int(input())
# Get_max(a,b)

#函数的返回值,可以返回想要的数据，不写返回则默认返回none
# def Get_max(a,b):
#     if a>=b:
#         print(f"最大的数为{a}")
#     else :
#         print(f"最大的数为{b}")
# a = 1
# b = 2
# number = Get_max(a,b)
# print(number)

#函数的全局变量和局部变量以及global改变全局变量的用法
# number = 200
#
# def num_cut():
#     number=100
#     number_2 = 500
#     print(number)
#     print(number_2)
# def num_turn():
#     global number
#     number = 1000
#     print(number)
# num_cut()
# num_turn()
# print(number)

#函数的综合使用案例取钱系统
money = 5000000
name = input("请输入你的名字：")
i = 1
def Get_money():
    global money
    print("您的账户余额为%d" %money)
def Cun_money(number):
    global money
    money += number
def Qu_money(number):
    global money
    money-=number
def main_enum():
    sign = input("请输入您选择的服务:")
    if sign=="查询余额":
        Get_money()
    elif sign=="存款":
        money_1 = int(input("请输入存款金额："))
        Cun_money(money_1)
        Get_money()
    elif sign=="取款":
        money_1 = int(input("请输入取款金额："))
        Qu_money(money_1)
        Get_money()
    else:
        global i
        i = 2
while i==1:
    main_enum()
