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

###統計量
arma_model.statistics()
### 打印出序列平均數與變異數 'Mean: 2.0000, Variance: 1.7500'


### 生成序列進行本地存擋file支援（csv, txt, xlsx）
arma.save(file_name = "your_file_name.xlsx")
arma.save(file_name = "your_file_name.csv")
arma.save(file_name = "your_file_name.txt")


```

