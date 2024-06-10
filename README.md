<tr>
  <h1>Python程式設計-期末報告 : 列印溫度轉換速查表</h1>
  <h3>11124232卓柏宇、11124230葉承諺</h3>
</tr>
  
<h2>描述</h2>
<h4>已知華氏溫度轉換攝氏溫度的計算公式：C=5×(F−32)/9，其中：C 表示攝氏溫度，F 表示華氏溫度。
  
編寫函數 F2C(f)將華氏溫度轉換為攝氏溫度，讀入兩個華氏溫度值 f1 和 f2，列印範圍在 f1~f2 內，每次增加兩個華氏溫度刻度的速查表。

  注意：如果 f1>f2，則直接列印 error。
</h4>
<h2>輸入格式</h2>
<h4>輸入為一行，為兩個不小於 32 的正整數 f1 和 f2，表示兩個華氏溫度。兩個數之間用逗號隔開，形如 f1,f2。</h4>
<h2>輸出格式</h2>
<h4>如果 f1>f2，輸出 error。

如果 f1<=f2，則輸出華氏轉攝氏的溫度轉換速查表，速查表可能有多行，每行一個溫度轉換對，形如 f1 : c1，其中 c1 保留小數點兩位。速查表以 2 華氏度為刻度。</h4>
<h2>範例 1</h2>

![image](https://github.com/qwertidy/final_report/blob/main/1.png)
<h2>範例 2</h2>

![image](https://github.com/qwertidy/final_report/blob/main/2.png)
<h2>範例 3</h2>

![image](https://github.com/qwertidy/final_report/blob/main/3.png)
<h2>範例 4</h2>

![image](https://github.com/qwertidy/final_report/blob/main/4.png)
<h2>範例 5</h2>

![image](https://github.com/qwertidy/final_report/blob/main/5.png)
<h2>程式碼使用VScode實作</h2>

```python
def F2C(f):
    c=5*(f-32)/9
    return c
print("輸入格式(int,int) :")
left,right=map(int,input().split (','))
print("-----------------------------")
if left>right:
    print('error')
else:
    for f in range(left,right+1,2):
        print("{}:{:.2f}".format(f,F2C(f)))
```


