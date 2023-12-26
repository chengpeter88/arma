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

---

## 使用手冊

該套件包括三個計量經濟學中常用的時間序列模型，可作為類別變數使用：

```python
from arma import ARMA
from arma import MA
from arma import AR

ARMA 模型

要創建一個 ARMA 模型實例，請如下初始化：

arma=ARMA(p=1, q=1, phi=[0.5], theta=[0.5], c=1.0, mu=0.0, sigma=1.0)
```
ARMA 模型的數學表示如下：

$$
X_{t} = c + \epsilon_{t} + \sum_{i=1}^{p} \phi_{i} X_{t-i} + \sum_{j=1}^{q} \theta_{j} \epsilon_{t-j}
$$


可參考網址詳細數學模型建構：https://zh.wikipedia.org/zh-tw/ARMA%E6%A8%A1%E5%9E%8B



其中針對屬性定義：

	•	p , q 為AR 與 MA 模型的階層數（order）
	•	phi 為建構p階層，所設立的係數。
 	•	theta 為建構q階層，所設立的係數
	•	c, mu 屬性為透過常態分配抽樣建立隨機誤差項N(c,,mu^2)，其中c為平均數，mu為標準差

 -----
 ## ARMA 模型instace method

```python
### ARMA模型生成資料長度 n = int
arma.simulate(n=100)

### 畫圖自動產生成資料圖形（ggplot）
arma.plot()
![image](https://github.com/chengpeter88/arma/assets/108580387/141b031a-ed1a-4dee-a7ed-714bbf7dc8c9)


###統計量
arma_model.statistics()
### 打印出序列平均數與變異數 'Mean: 2.0000, Variance: 1.7500'


### 生成序列進行本地存擋file支援（csv, txt, xlsx）
arma.save(file_name = "your_file_name.xlsx")
arma.save(file_name = "your_file_name.csv")
arma.save(file_name = "your_file_name.txt")


```


當然可以，以下是一個完整的 Markdown 文件範例，做了一些調整來改善格式和清晰度：

```markdown
# ARMA, AR, MA 模型

此套件包含三種計量經濟學中常見的時間序列模型：ARMA, AR, 和 MA，作為類別變數提供。

## 安裝方法

要安裝此套件，請在命令行運行以下命令：

```bash
pip install git+https://github.com/chengpeter88/arma@v1.0.3
```

## 解除安裝方法

要解除安裝此套件，請運行：

```bash
pip uninstall arma
```

---

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

## Instance Methods

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

### 圖形展示

圖形展示的功能需要將圖形保存在您的 GitHub 倉庫中的某個位置，然後使用相對路徑或絕對路徑來引用它。以下是一個圖片的 Markdown 引用示例：

```markdown
![ARMA Model Data Plot](/path/to/your/image.png)
```

請將 `/path/to/your/image.png` 替換為您圖片的實際路徑。

注意：Markdown 文件中的 LaTeX 數學公式可能不會在所有平台上正確渲染，這取決於該平台對 LaTeX 的支持程度。
```

請將這個範本內容替換為您的 `README.md` 文件內容，並根據需要進行適當的調整。特別注意圖片路徑應該指向實際的圖片位置，並且確認您的 GitHub 倉庫結

