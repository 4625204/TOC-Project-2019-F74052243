# 計算理論作業 F74052243 資訊109 孫名柔 

## chat bot 說明
這是一個可以搜尋名偵探柯南電影版的chat bot
### 1.首先輸入數字「x」(範圍：01~10)：
就會回答第x部柯南電影版的名稱，並進入此部電影版的狀態
### 2.接下來可以選擇輸入「腳本」或「主題曲」或「海報」：
若輸入「腳本」就會回答此部電影版的腳本製作人
輸入「主題曲」就會回答此部電影版的主題曲名稱及演唱者
輸入「海報」就會跳出此電影版的海報
### 3.在1,2,階段皆可輸入「回」：
它會回覆「ok」，這樣便會結束此部電影版的詢問回到最初狀態，可以選擇輸入下一步電影版的數字

## example

![](https://i.imgur.com/TWbiarb.png)
![](https://i.imgur.com/CH2xWT9.png)


## state 說明
### initial state :user
### state1～10:statex,代表回覆第x部柯南電影版名稱
### state11,21......101:x1,代表回覆第x部腳本製作人
### state12,22......102:x2,代表回覆第x部主題曲名稱及演唱者
### stateimg1,2......10:stateimgx,代表回覆第x部電影版的海報
### stateback:回答ok,去user（go_back）

## final state 圖
### http://localhost:5000/show-fsm
