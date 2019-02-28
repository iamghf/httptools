#! /usr/bin/env
# endcoding:utf-8
# author ghf
import urllib2
import urllib
import cookielib
import json
import tkinter as tk
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

urls={
    'local':'http://127.0.0.1:50001/CRMService',
    'dev':'http://10.3.3.180:50001/CRMService',
    'test':'http://10.3.3.199:50001/CRMService',
    'uat':'http://10.3.3.182:50001/CRMService'
}

headers={'Content-Type':'application/json'}

def do_post(url,data):
    request = urllib2.Request(url=url, headers=headers, data=data)
    response = urllib2.urlopen(request)
    #print(response.read())
    return response

def reset(text1,text2):
    text1.delete('1.0','end')
    text2.delete('1.0', 'end')

def show_result(url,inText,outText):
    jsonData = inText.get('1.0','end')
    outText.delete('1.0','end')
    resp = do_post(url,jsonData)
    #outText.insert('end',inText.get('1.0','end'))
    str = json.dumps(json.loads(jsonData),ensure_ascii=False,sort_keys=True, indent=4)
    inText.delete('1.0','end')
    inText.insert('end',str)
    outText.insert('end', json.dumps(json.load(resp),ensure_ascii=False,sort_keys=True, indent=4))

def draw():
    window = tk.Tk()
    window.title('接口测试')
    #window.geometry('640x550')
    window.resizable(width=False, height=False)

    frmLT = tk.Frame(width=680, height=30, bg='white')
    frmLC = tk.Frame(width=630, height=450, bg='grey')
    frmLB = tk.Frame(width=680, height=40,bg='white')
    #frmRT = tk.Frame(width=200, height=500,bg='black')

    frmLT.grid(row=0, column=0, padx=1, pady=3)
    frmLC.grid(row=1, column=0, padx=1, pady=3)
    frmLB.grid(row=2, column=0)
    #frmRT.grid(row=0, column=1, rowspan=3, padx=2, pady=3)

    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    #frmRT.grid_propagate(0)

    lable = tk.Label(frmLT, text='服务地址:', font=('微软雅黑', 10))
    lable.grid(row=0, column=0,sticky='W')
    entry = tk.Entry(frmLT, font=('微软雅黑', 14),width=66)
    entry.grid(row=0, column=1,columnspan=7,sticky='E')
    entry.insert('end',urls['test'])

    inText = tk.Text(frmLC, font=('微软雅黑', 8), width=60, height=43)
    inText.grid(row=1, column=0,padx=3, pady=3)
    outText = tk.Text(frmLC, font=('微软雅黑', 8), width=60, height=43)
    outText.grid(row=1, column=1,padx=3, pady=3)

    button = tk.Button(frmLB, text='提交', width=30, font=('微软雅黑', 10),command=lambda: show_result(entry.get(), inText, outText))
    button.grid(row=2, column=0,padx=100, pady=3)
    button1 = tk.Button(frmLB, text='重置', width=30, font=('微软雅黑', 10), command=lambda: reset(inText, outText))
    button1.grid(row=2, column=1,padx=10, pady=3)

    window.mainloop()

def main():
    draw()

if __name__ == '__main__':
    main()
