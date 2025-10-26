import time
import numpy as np


# ---------------------- 基础工具函数 ----------------------
def matrix_add(A, B):
    """矩阵加法：计算两个n×n矩阵A与B的和"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def matrix_sub(A, B):
    """矩阵减法：计算两个n×n矩阵A与B的差"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def generate_random_matrix(n):
    """生成n×n随机矩阵，元素范围为0-9（便于验证结果）"""
    return [[np.random.randint(0, 10) for _ in range(n)] for _ in range(n)]


def print_matrix(mat, name="Matrix"):
    """打印矩阵（用于输出运算结果）"""
    print(f"\n{name}:")
    for row in mat:
        print(row)


# ---------------------- 传统矩阵乘法实现 ----------------------
def traditional_matrix_mult(A, B):
    """传统矩阵乘法：时间复杂度O(n³)"""
    n = len(A)
    # 初始化结果矩阵C
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            # 缓存A[i][k]，减少重复索引访问
            a_ik = A[i][k]
            for j in range(n):
                C[i][j] += a_ik * B[k][j]
    return C


# ---------------------- 分治法矩阵乘法实现 ----------------------
def divide_conquer_mult(A, B):
    """分治法矩阵乘法：时间复杂度O(n³)，分治思想实现"""
    n = len(A)
    # 基准情况：1×1矩阵直接相乘
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # 分割矩阵（假设n为2的幂，非2的幂可补0扩展，此处简化处理）
    mid = n // 2
    # 分割矩阵A为4个子矩阵
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    # 分割矩阵B为4个子矩阵
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # 递归计算子矩阵乘积与加法
    C11 = matrix_add(divide_conquer_mult(A11, B11), divide_conquer_mult(A12, B21))
    C12 = matrix_add(divide_conquer_mult(A11, B12), divide_conquer_mult(A12, B22))
    C21 = matrix_add(divide_conquer_mult(A21, B11), divide_conquer_mult(A22, B21))
    C22 = matrix_add(divide_conquer_mult(A21, B12), divide_conquer_mult(A22, B22))

    # 合并4个子矩阵为结果矩阵C
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])  # 上半部分：C11行 + C12行
    for i in range(mid):
        C.append(C21[i] + C22[i])  # 下半部分：C21行 + C22行
    return C


# ---------------------- 拓展实验：Strassen算法实现 ----------------------
def strassen_mult(A, B):
    """Strassen算法矩阵乘法：时间复杂度O(n^log2⁷)≈O(n².81)"""
    n = len(A)
    # 基准情况：1×1矩阵直接相乘
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # 分割矩阵（辅助函数简化代码）
    mid = n // 2
    A11, A12, A21, A22 = split_matrix(A, mid)
    B11, B12, B21, B22 = split_matrix(B, mid)

    # 计算7个中间矩阵（减少乘法次数）
    M1 = strassen_mult(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_mult(matrix_add(A21, A22), B11)
    M3 = strassen_mult(A11, matrix_sub(B12, B22))
    M4 = strassen_mult(A22, matrix_sub(B21, B11))
    M5 = strassen_mult(matrix_add(A11, A12), B22)
    M6 = strassen_mult(matrix_sub(A21, A11), matrix_add(B11, B12))
    M7 = strassen_mult(matrix_sub(A12, A22), matrix_add(B21, B22))

    # 由中间矩阵计算结果子矩阵
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_sub(matrix_add(M1, M3), M2), M6)

    # 合并子矩阵为最终结果
    return merge_matrix(C11, C12, C21, C22, mid)


def split_matrix(mat, mid):
    """Strassen算法辅助函数：分割矩阵为4个子矩阵"""
    n = len(mat)
    top_left = [row[:mid] for row in mat[:mid]]
    top_right = [row[mid:] for row in mat[:mid]]
    bottom_left = [row[:mid] for row in mat[mid:]]
    bottom_right = [row[mid:] for row in mat[mid:]]
    return top_left, top_right, bottom_left, bottom_right


def merge_matrix(C11, C12, C21, C22, mid):
    """Strassen算法辅助函数：合并4个子矩阵为完整矩阵"""
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C


# ---------------------- 实验主函数（执行测试与输出） ----------------------
def matrix_mult_experiment():
    """实验主函数：测试不同规模矩阵的三种乘法算法，输出结果与时间"""
    # 定义待测试的矩阵规模（选取2的幂，适配分治与Strassen算法）
    test_sizes = [2, 4, 8, 16, 32, 64]
    # 输出表头
    print("=" * 100)
    print("分治法解决矩阵乘法问题实验结果")
    print("=" * 100)
    print(
        f"{'矩阵规模(n×n)':<15}{'传统方法时间(ms)':<20}{'分治法时间(ms)':<20}{'Strassen时间(ms)':<20}{'结果一致性':<10}")
    print("-" * 100)

    for n in test_sizes:
        # 1. 生成随机测试矩阵
        A = generate_random_matrix(n)
        B = generate_random_matrix(n)

        # 2. 传统矩阵乘法：计算+计时
        start_time = time.time()
        C_traditional = traditional_matrix_mult(A, B)
        time_traditional = (time.time() - start_time) * 1000  # 转换为毫秒

        # 3. 分治法矩阵乘法：计算+计时
        start_time = time.time()
        C_divide = divide_conquer_mult(A, B)
        time_divide = (time.time() - start_time) * 1000

        # 4. Strassen算法乘法：计算+计时
        start_time = time.time()
        C_strassen = strassen_mult(A, B)
        time_strassen = (time.time() - start_time) * 1000

        # 5. 验证结果一致性（避免算法逻辑错误）
        result_consistent = "一致" if C_traditional == C_divide == C_strassen else "不一致"

        # 6. 输出当前规模的实验数据
        print(f"{n:<15}{time_traditional:<20.2f}{time_divide:<20.2f}{time_strassen:<20.2f}{result_consistent:<10}")

        # 7. （可选）打印小规模矩阵的具体结果（便于人工验证）
        if n <= 8:
            print_matrix(A, f"矩阵A({n}×{n})")
            print_matrix(B, f"矩阵B({n}×{n})")
            print_matrix(C_traditional, f"乘积矩阵C({n}×{n})")
            print("-" * 80)

    # 实验结束提示
    print("=" * 100)
    print("实验完成！可通过增大test_sizes中的规模（如128、256）进一步分析时间变化。")
    print("=" * 100)


# ---------------------- 执行实验 ----------------------
if __name__ == "__main__":
    matrix_mult_experiment()