# ARMA, AR, MA 模型

此套件包含三種計量經濟學中常見的時間序列模型，作為類別變數提供。

## 安裝方法

要安裝套件，請運行以下命令：
```
pip install git+https://github.com/chengpeter88/arma@v1.0.3
```

## 解除安裝方法

要解除安裝套件，請使用：
```
pip uninstall arma
```

-----------------------------

## 使用手冊

此套件提供了三個主要類別：`ARMA`, `AR`, 和 `MA`。以下是如何使用它們：

### ARMA 模型

```python
from arma import ARMA

# 初始化 ARMA 模型
arma = ARMA(p=1, q=1, phi=[0.5], theta=[0.5], c=1.0, mu=0.0, sigma=1.0)
```

ARMA 模型的數學表示如下：

$$
X_{t} = c + \epsilon_{t} + \sum_{i=1}^{p} \phi_{i} X_{t-i} + \sum_{j=1}^{q} \theta_{j} \epsilon_{t-j}
$$

進一步關於數學模型的詳細資訊，請參見[ARMA模型維基百科頁面](https://zh.wikipedia.org/zh-tw/ARMA%E6%A8%A1%E5%9E%8B)。

其中針對屬性定義：

	•	p , q 為AR 與 MA 模型的階層數（order）
	•	phi 為建構p階層，所設立的係數。
 	•	theta 為建構q階層，所設立的係數
	•	c, mu 屬性為透過常態分配抽樣建立隨機誤差項  N(c, mu^2) : 其中c為平均數 、 mu為標準差

### AR 模型

```python
from arma import AR

# 初始化 AR 模型
ar = AR(p=1, phi=[0.5], c=1.0, mu=0.0, sigma=1.0)
```

### MA 模型

```python
from arma import MA

# 初始化 MA 模型
ma = MA(q=1, theta=[0.5], mu=0.0, sigma=1.0)
```

---

## 實體方法（Instance Methods）

### 生成資料

```python
# 生成資料長度為 100 的 ARMA 模型數據
arma_data = arma.simulate(n=100)
```

### 繪製資料圖形

```python
# 繪製 ARMA 模型數據圖形
arma.plot()
```

### 統計量分析

```python
# 獲取 ARMA 模型數據的統計量
arma_statistics = arma.statistics()
```

### 保存數據

```python
# 將 ARMA 模型數據保存為 CSV 文件
arma.save(file_name="arma_data.csv")
```

### 圖形plot()
以下展示為透過`arma.plot()` 實體後可以獲取的圖片：


![ARMA Model Data Plot](https://github.com/chengpeter88/arma/raw/master/arma_demo.png)





