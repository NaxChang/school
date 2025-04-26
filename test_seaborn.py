import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")
# 生成測試數據
tips = sns.load_dataset("tips")

# 繪製圖表
sns.histplot(tips["total_bill"], bins=20)
plt.show()
plt.savefig("output.png")
