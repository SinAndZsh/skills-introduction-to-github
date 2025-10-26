import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 设置中文字体 - 避免使用特殊符号
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel('身高预测数据.xlsx')

# 提取数据
foot_length = df['足长'].values.reshape(-1, 1)
stride = df['步幅'].values.reshape(-1, 1)
height = df['身高'].values

# 计算回归模型
model_foot = LinearRegression()
model_foot.fit(foot_length, height)
height_pred_foot = model_foot.predict(foot_length)
r2_foot = r2_score(height, height_pred_foot)

model_stride = LinearRegression()
model_stride.fit(stride, height)
height_pred_stride = model_stride.predict(stride)
r2_stride = r2_score(height, height_pred_stride)

# 学号姓名信息
student_info = "学号: 230511637 姓名: 张世浩"

print("开始绘制图表...")

# ========== 题目1：足长和身高的散点图 ==========
print("绘制题目1：足长散点图...")
plt.figure(figsize=(10, 6))
plt.scatter(foot_length, height, alpha=0.6, color='blue')
plt.xlabel('足长 (cm)')
plt.ylabel('身高 (cm)')
plt.title('题目1：足长和身高的散点图')
plt.grid(True, alpha=0.3)
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 题目1：步幅和身高的散点图 ==========
print("绘制题目1：步幅散点图...")
plt.figure(figsize=(10, 6))
plt.scatter(stride, height, alpha=0.6, color='orange')
plt.xlabel('步幅 (cm)')
plt.ylabel('身高 (cm)')
plt.title('题目1：步幅和身高的散点图')
plt.grid(True, alpha=0.3)
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 题目2：足长和身高的线性回归模型 ==========
print("绘制题目2：足长线性回归...")
plt.figure(figsize=(10, 6))
plt.scatter(foot_length, height, alpha=0.6, color='blue', label='实际数据')
plt.plot(foot_length, height_pred_foot, color='red', linewidth=2, label='拟合直线')
plt.xlabel('足长 (cm)')
plt.ylabel('身高 (cm)')
plt.title(f'题目2：足长和身高的线性回归模型\n拟合方程: y = {model_foot.coef_[0]:.4f}x + {model_foot.intercept_:.4f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 题目3：步幅和身高的线性回归模型 ==========
print("绘制题目3：步幅线性回归...")
plt.figure(figsize=(10, 6))
plt.scatter(stride, height, alpha=0.6, color='orange', label='实际数据')
plt.plot(stride, height_pred_stride, color='green', linewidth=2, label='拟合直线')
plt.xlabel('步幅 (cm)')
plt.ylabel('身高 (cm)')
plt.title(f'题目3：步幅和身高的线性回归模型\n拟合方程: y = {model_stride.coef_[0]:.4f}x + {model_stride.intercept_:.4f}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 题目4：两个模型的准确率对比 ==========
print("绘制题目4：模型准确率对比...")
plt.figure(figsize=(10, 6))
models = ['足长-身高模型', '步幅-身高模型']
r2_scores = [r2_foot, r2_stride]
colors = ['lightblue', 'lightcoral']

bars = plt.bar(models, r2_scores, color=colors, alpha=0.7, edgecolor='black')
plt.ylabel('R2 决定系数')  # 使用 R2 而不是 R²
plt.title('题目4：两个线性回归模型的准确率对比')
plt.ylim(0, 1)

# 在柱状图上显示数值
for bar, score in zip(bars, r2_scores):
    height_bar = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height_bar + 0.01,
             f'{score:.4f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.grid(True, alpha=0.3, axis='y')
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 题目5：模型效果分析 ==========
print("绘制题目5：模型效果分析...")
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.scatter(foot_length, height, alpha=0.4, color='blue', label='足长数据')
plt.plot(foot_length, height_pred_foot, color='red', linewidth=2, label='足长拟合线')
plt.xlabel('足长 (cm)')
plt.ylabel('身高 (cm)')
plt.title('足长-身高模型拟合效果')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.scatter(stride, height, alpha=0.4, color='orange', label='步幅数据')
plt.plot(stride, height_pred_stride, color='green', linewidth=2, label='步幅拟合线')
plt.xlabel('步幅 (cm)')
plt.ylabel('身高 (cm)')
plt.title('步幅-身高模型拟合效果')
plt.legend()
plt.grid(True, alpha=0.3)

better_model = "足长-身高模型" if r2_foot > r2_stride else "步幅-身高模型"
plt.suptitle(f'题目5：模型效果分析\n最佳模型: {better_model} (R2较高)')  # 使用 R2 而不是 R²
plt.figtext(0.5, 0.01, student_info, ha='center', fontsize=10, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# ========== 输出详细结果 ==========
print("=" * 60)
print("                   实验成果总结")
print("=" * 60)

print(f"\n【题目2：足长-身高线性回归模型】")
print(f"拟合直线方程: 身高 = {model_foot.coef_[0]:.4f} × 足长 + {model_foot.intercept_:.4f}")
print(f"R2 决定系数: {r2_foot:.4f}")

print(f"\n【题目3：步幅-身高线性回归模型】")
print(f"拟合直线方程: 身高 = {model_stride.coef_[0]:.4f} × 步幅 + {model_stride.intercept_:.4f}")
print(f"R2 决定系数: {r2_stride:.4f}")

print(f"\n【题目4：模型准确率】")
print(f"足长-身高模型 R2: {r2_foot:.4f}")
print(f"步幅-身高模型 R2: {r2_stride:.4f}")

print(f"\n【题目5：模型效果分析】")
if r2_foot > r2_stride:
    print("✅ 足长-身高模型的预测效果更好")
    print(f"   足长模型的R2比步幅模型高 {r2_foot - r2_stride:.4f}")
else:
    print("✅ 步幅-身高模型的预测效果更好")
    print(f"   步幅模型的R2比足长模型高 {r2_stride - r2_foot:.4f}")

print(f"\n结论：基于R2决定系数，{'足长' if r2_foot > r2_stride else '步幅'}作为自变量的")
print("      线性回归模型在身高预测任务中表现更优。")