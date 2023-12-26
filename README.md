# <span style="color:yellow">ARMA, AR, MA process</span>
## install 下載套件方式
--------
```
pip install git+https://github.com/chengpeter88/arma@v1.0.0
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

其中數學參數定義如下架設
-  其中：c是常數項、\varepsilon _{t}被假設為平均數等於0，標準差等於 \sigma 的隨機誤差值；\varepsilon _{t}被假設為對於任何的t都不變。
