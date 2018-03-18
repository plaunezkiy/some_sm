#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from math import cos, sin, radians, sqrt, degrees, acos, ceil
from tkinter import Canvas
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkm

global a, b, c, al, be, ce
def pos(a, b, c, al, be, ce):
    i = 370
    o = 20
    if be > 90:
        x = cos(radians(180 - be)) * c
        y = sin(radians(180 - be)) * c
        x += i
        y += o
    if al > 90:
        x = sin(radians(90 - be)) * c
        y = cos(radians(90 - be)) * c
        x += i
        y += o
    if ce > 90:
        x = cos(radians(180 - ce)) * b
        y = sin(radians(180 - ce)) * b
        x = x + i + a
        y = o + y
        canvas.create_line(i, y, x, o, width=3, fill='green')      # CA
        canvas.create_line(i, y, i + a, y, width=3, fill='green')  # CB
        canvas.create_line(x, o, i + a, y, width=3, fill='green')  # AB
        canvas.create_text(i - 7, y + 5, text='C')
        canvas.create_text(x, o - 12, text='A')
        canvas.create_text(i + a, y + 7, text='B')
    else:
        x = sin(radians(90 - be)) * c
        y = cos(radians(90 - be)) * c
        x = x + i
        a += i
        y += o
        canvas.create_line(i, y, x, o, width=3, fill='green')  # BA
        canvas.create_line(i, y, a, y, width=3, fill='green')  # BC
        canvas.create_line(x, o, a, y, width=3, fill='green')  # AC
        canvas.create_text(i - 7, y + 5, text='B')
        canvas.create_text(x - 5, o - 7, text='A')
        canvas.create_text(a + 5, y + 5, text='C')
    canvas.pack()


def resh(a, b, c, al, be, ce):
    try:
        if al and be and not ce:
            ce = 180 - (al + be)
        if al and ce and not be:
            be = 180 - (al + ce)
        if be and ce and not al:
            al = 180 - (ce + be)
        if al and be and not ce:
            ce = 180 - (al + be)
        if al and ce and not be:
            be = 180 - (al + ce)
        if be and ce and not al:
            al = 180 - (ce + be)
        ####
        cc = radians(ce)
        aa = radians(al)
        bb = radians(be)
        cosce = cos(cc)
        since = sin(cc)
        cosal = cos(aa)
        sinal = sin(aa)
        cosbe = cos(bb)
        sinbe = sin(bb)
        ####
        if c and a and not b and be:
            d = (a ** 2 + c ** 2 - 2 * a * c * cosbe)
            b = sqrt(d)
        if a and b and ce and not c:
            d = a ** 2 + b ** 2 - 2 * a * b * cosce
            c = sqrt(d)

        if b and c and al and not a:
            d = b ** 2 + c ** 2 - 2 * c * b * cosal
            a = sqrt(d)

        if a and c and be and not b:
            d = a ** 2 + c ** 2 - 2 * a * c * cosbe
            a = sqrt(d)
        ####
        if not a and be and b and al:
            a = b * sinal / sinbe
        elif not a and ce and c and al:
            a = c * sinal / since

        if not b and al and a and be:
            b = a * sinbe / sinal
        elif not be and ce and c and be:
            b = c * sinbe / since

        if not c and al and a and ce:
            c = a * since / sinal
        elif not c and ce and b and be:
            c = b * since / sinbe
        ####
        if a and b and ce and not c:
            d = a ** 2 + b ** 2 - 2 * a * b * cosce
            c = sqrt(d)

        if b and c and al and not a:
            d = b ** 2 + c ** 2 - 2 * c * b * cosal
            a = sqrt(d)

        if not a and c and be and not b:
            d = a ** 2 + c ** 2 - 2 * a * c * cosbe
            a = sqrt(d)
        ####
        if a and b and c and not al:
            cosal = -(a ** 2 - b ** 2 - c ** 2) / (2 * c * b)
            al = acos(cosal)
            al = degrees(al)
        if a and b and c and not be:
            cosbe = -(b ** 2 - c ** 2 - a ** 2) / (2 * a * c)
            be = acos(cosbe)
            be = degrees(be)
        if a and b and c and not ce:
            cosce = -(c ** 2 - b ** 2 - a ** 2) / (2 * a * b)
            ce = acos(cosce)
            ce = degrees(ce)
        ####
        if a and b and c and not al:
            cosal = -(a ** 2 - b ** 2 - c ** 2) / (2 * c * b)
            al = acos(cosal)
            al = degrees(al)
        if a and b and c and not be:
            cosbe = -(b ** 2 - c ** 2 - a ** 2) / (2 * a * c)
            be = acos(cosbe)
            be = degrees(be)
        if a and b and c and not ce:
            cosce = -(c ** 2 - b ** 2 - a ** 2) / (2 * a * b)
            ce = acos(cosce)
            ce = degrees(ce)
        if c and a and not b and be:
            d = (a ** 2 + c ** 2 - 2 * a * c * cosbe)
            b = sqrt(d)
            
        ce = radians(ce)
        al = radians(al)
        be = radians(be)
        since = sin(ce)
        sinal = sin(al)
        sinbe = sin(be)
        p = (a + b + c) * 0.5
        s = p * (p - a) * (p - b) * (p - c)  # 3.9375
        sal = ((c * b * sinal) / 2) ** 2
        sce = ((a * b * since) / 2) ** 2        # 3*
        sbe = ((a * c * sinbe) / 2) ** 2
        
        if not (1 >= sal - s >= -1) \
                or not (1 >= sce - s >= -1) or not (1 >= sbe - s >= -1):
            a = 0
            b = 0
            c = 0
            al = 0
            be = 0
            ce = 0
        al = degrees(al)
        be = degrees(be)
        ce = degrees(ce)
        if a + b < c or a + c < b or b + c < a:
            a = 0
            b = 0
            c = 0
            al = 0
            be = 0
            ce = 0
    except ValueError:
        a = 0
        b = 0
        c = 0
        al = 0
        be = 0
        ce = 0
    return a, b, c, al, be, ce


def bub():
    a = A.get()
    b = B.get()
    c = C.get()
    al = AL.get()
    be = BE.get()
    ce = CE.get()
    if a == '':
        a = 0
    if b == '':
        b = 0
    if c == '':
        c = 0
    if al == '':
        al = 0
    if be == '':
        be = 0
    if ce == '':
        ce = 0
    a = float(a)
    b = float(b)
    c = float(c)
    al = float(al)
    be = float(be)
    ce = float(ce)
    x = list(resh(a, b, c, al, be, ce))
    a = x[0]
    b = x[1]
    c = x[2]
    al = x[3]
    be = x[4]
    ce = x[5]
    if a and b and c and al and be and ce:
        c_ent.insert(0, round(c, 2))
        a_ent.insert(0, round(a, 2))
        b_ent.insert(0, round(b, 2))
        ce_ent.insert(0, round(ce, 2))
        al_ent.insert(0, round(al, 2))
        be_ent.insert(0, round(be, 2))
        if a < 90 or b < 90 or c < 90:
            d = 120 // a
            a *= d
            b *= d
            c *= d
        elif a > 150 or b > 150 or c > 150:
            d = ceil(a / 150)
            a = a / d
            b = b / d
            c = c / d
        ttk.Button(root, text='Построить', command=lambda: pos(a, b, c, al, be, ce)).place(x=0, y=115, width=210, height=40)       #pos(a, b, c, al, be, ce)
    else:
        tkm.showerror("Ошибка!", "Треугольник не существует или недостаточно данных!")


def p():
    canvas.delete(ALL)
    rebus()

def copy(a,b,c,al,be,ce):
    print(a)
    root.clipboard_clear()
    #root.clipboard_append("AB={}, BC={}, AC={}, ∠ACB={}, ∠BAC={}, ∠ABC={}".format(c,a,b,ce,al,be))
    root.clipboard_append(a)


root = Tk()
root.geometry("800x300")
root.resizable(width=False, height=False)
icon = tk.PhotoImage(file = r'icon.ico')
root.tk.call('wm', 'iconphoto', root._w, icon)
root.title('Plaungles')
coc = '#d8f2e8'  # 507fb7
canvas = Canvas(root, width=800, height=300, bg=coc)


def rebus():
    canvas.create_line(275, 10, 225, 80, width=3.25)    # (50,10,0,80)
    canvas.create_line(275, 10, 320, 100, width=3.25)   # (50,10,95,100)
    canvas.create_line(225, 80, 320, 100, width=3.25)   # (0,80,95,100)
    Label(root, text='A', bg=coc, font='Lobster 10').place(x=278, y=3, height=10)
    Label(root, text='B', bg=coc, font='Lobster 10').place(x=211, y=75, height=10)
    Label(root, text='C', bg=coc, font='Lobster 10').place(x=320, y=97, height=10)
    global A, B, C, AL, BE, CE
    A = StringVar()
    B = StringVar()
    C = StringVar()
    AL = StringVar()
    BE = StringVar()
    CE = StringVar()
    hx = 'light blue'
    global c_ent, a_ent, b_ent, ce_ent, al_ent, be_ent
    c_ent = Entry(textvariable=C, bg=hx)
    c_ent.place(x=50, y=0, width=50, height=25)
    c_ent.focus_set()
    ####
    a_ent = Entry(textvariable=A, bg=hx)
    a_ent.place(x=50, y=25, width=50, height=25)
    ####
    b_ent = Entry(textvariable=B, bg=hx)
    b_ent.place(x=50, y=50, width=50, height=25)
    ####
    ce_ent = Entry(textvariable=CE, bg=hx)
    ce_ent.place(x=160, y=0, width=50, height=25)
    ####
    al_ent = Entry(textvariable=AL, bg=hx)
    al_ent.place(x=160, y=25, width=50, height=25)
    ####
    be_ent = Entry(textvariable=BE, bg=hx)
    be_ent.place(x=160, y=50, width=50, height=25)
    ####
    Label(root, text='AB =', font='Arial 10', bg=coc).place(x=0, y=0, width=50, height=25)
    Label(root, text='BC =', font='Arial 10', bg=coc).place(x=0, y=25, width=50, height=25)
    Label(root, text='AC =', font='Arial 10', bg=coc).place(x=0, y=50, width=50, height=25)
    Label(root, text='∠ACB =', font='Arial 10', bg=coc).place(x=100, y=0, width=60, height=25)
    Label(root, text='∠BAC =', font='Arial 10', bg=coc).place(x=100, y=25, width=60, height=25)
    Label(root, text='∠ABC =', font='Arial 10', bg=coc).place(x=100, y=50, width=60, height=25)
    qit = ttk.Button(root, text='Выйти', command=lambda: root.destroy()).place(x=700, y=270, width=100, height=30)
    rest = ttk.Button(root, text='Очистить', command=lambda: p()).place(x=600, y=270, width=100, height=30)
    but = ttk.Button(root, text='Решить', command=lambda: bub())
    #cope = ttk.Button(root, text='Скопировать конфиг', command=lambda a,b,c,al,be,ce: copy(a,b,c,al,be,ce)).place(x=0, y=270, width=150, height=30)
    but.place(x=0, y=75, width=210, height=40)
    canvas.pack()


rebus()
root.mainloop()
