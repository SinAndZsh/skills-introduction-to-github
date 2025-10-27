def lcs_length(x, y):
    """计算最长公共子序列长度并返回动态规划表"""
    m = len(x)
    n = len(y)
    # 创建(m+1)x(n+1)的动态规划表，初始值为0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # 字符匹配，长度为左上角值+1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 字符不匹配，取上方或左方的最大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp


def get_lcs(x, y, dp):
    """根据动态规划表回溯获取最长公共子序列"""
    i, j = len(x), len(y)
    lcs = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            # 字符匹配，加入LCS
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # 上方值更大，向上移动
            i -= 1
        else:
            # 左方值更大，向左移动
            j -= 1
    # 反转得到正确顺序
    return ''.join(reversed(lcs))


def hybrid_fruit_name(fruit1, fruit2):
    """杂交水果命名算法：生成包含两个水果名作为子序列的最短字符串"""
    # 计算LCS
    dp = lcs_length(fruit1, fruit2)
    lcs = get_lcs(fruit1, fruit2, dp)

    # 构建杂交名称
    result = []
    i = j = k = 0  # 分别为fruit1, fruit2, lcs的指针

    while k < len(lcs):
        # 添加fruit1中到当前LCS字符前的所有字符
        while i < len(fruit1) and fruit1[i] != lcs[k]:
            result.append(fruit1[i])
            i += 1
        # 添加fruit2中到当前LCS字符前的所有字符
        while j < len(fruit2) and fruit2[j] != lcs[k]:
            result.append(fruit2[j])
            j += 1
        # 添加LCS字符（公共部分只加一次）
        result.append(lcs[k])
        i += 1
        j += 1
        k += 1

    # 添加剩余字符
    result.extend(fruit1[i:])
    result.extend(fruit2[j:])

    return ''.join(result)


def main():
    # 输入两个字符序列
    x = input("请输入第一个字符序列: ")
    y = input("请输入第二个字符序列: ")

    # 计算LCS相关结果
    dp = lcs_length(x, y)
    lcs = get_lcs(x, y, dp)
    lcs_len = dp[len(x)][len(y)]

    # 输出动态规划表
    print("\n动态规划数组（最长公共子序列长度）:")
    for row in dp:
        print(row)

    # 输出LCS结果
    print(f"\n最长公共子序列长度: {lcs_len}")
    print(f"最长公共子序列: {lcs}")

    # 算法复杂度分析
    print("\n算法复杂度分析:")
    print(f"时间复杂度: O(m*n)，其中m={len(x)}, n={len(y)}")
    print(f"空间复杂度: O(m*n)（动态规划表存储）")

    # 杂交水果命名示例
    print("\n杂交水果命名示例:")
    fruit1 = "apple"
    fruit2 = "peach"
    hybrid = hybrid_fruit_name(fruit1, fruit2)
    print(f"{fruit1} 和 {fruit2} 的杂交水果名为: {hybrid}")

    # 自定义杂交水果命名
    fruit_a = input("\n请输入第一种水果名称: ")
    fruit_b = input("请输入第二种水果名称: ")
    print(f"杂交水果名为: {hybrid_fruit_name(fruit_a, fruit_b)}")


if __name__ == "__main__":
    main()