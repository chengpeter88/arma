# <span style="color:yellow">ARMA, AR, MA process</span>
## install 下載套件方式
--------
```
pip install git+https://github.com/chengpeter88/arma@v1.0.3
```
## uninstall 下載套件方式
```
pip uninstall arma
```
-----
## handbook 套件使用方式
套件中有三個計量經濟中常見時間序列模型（三個類變數）
使用者只需透過以下指令可以呼叫套件類變數
```
from arma import ARMA
from arma import MA
from arma import AR 
```
## ARMA 
```
ARMA(p=1, q=1,phi=[0.5],theta=[0.5],c=1.0,mu=0.0,sigma=1.0)
```

$$
X_{t} = c + \epsilon_{t} + \sum_{i=1}^{p} \phi_{i} X_{t-i} + \sum_{j=1}^{q} \theta_{j} \epsilon_{t-j}
$$
--------
其中數學參數定義如下架設
-  其中：c是常數項、$\varepsilon _{t}$被假設為平均數等於0，標準差等於 \sigma 的隨機誤差值；\varepsilon _{t}被假設為對於任何的t都不變。




# ARMA, AR, MA 過程

此套件包含三種計量經濟學中常見的時間序列模型，作為類別變數提供。

## 安裝方法

要安裝套件，請運行以下命令：

pip install git+https://github.com/chengpeter88/arma@v1.0.3

## 解除安裝方法

要解除安裝套件，請使用：

pip uninstall arma

---

## 使用手冊

該套件包括三個計量經濟學中常用的時間序列模型，可作為類別變數使用：

```python
from arma import ARMA
from arma import MA
from arma import AR

ARMA 模型

要創建一個 ARMA 模型實例，請如下初始化：

ARMA(p=1, q=1, phi=[0.5], theta=[0.5], c=1.0, mu=0.0, sigma=1.0)

ARMA 模型的數學表示如下：

$$
X_{t} = c + \epsilon_{t} + \sum_{i=1}^{p} \phi_{i} X_{t-i} + \sum_{j=1}^{q} \theta_{j} \epsilon_{t-j}
$$

其中：

	•	c 是常數項
	•	\epsilon_{t} 假設為平均數為 0 且標準差為 \sigma 的隨機誤差
	•	對於任何 t，\epsilon_{t} 被假設為恆定不變。

