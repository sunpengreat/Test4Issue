def calculate_average(numbers):

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # 获取要输入的数字个数
    n = int(input("请输入数字的个数: "))

    numbers = []
    print(f"请输入 {n} 个数字:")

    # 循环读取 n 个数字
    for i in range(n):
        num = float(input(f"第 {i+1} 个数字: "))
        numbers.append(num)

    # 计算平均值
    result = calculate_average(numbers)

    # 输出结果
    print(f"\n数字列表: {numbers}")
    print(f"平均数: {result:.2f}")
