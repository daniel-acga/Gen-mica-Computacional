#!/usr/bin/env python
# coding: utf-8

# # Genómica Computacional
# Práctica 02 - Herramientas bioinformáticas (Python)
# 
# 

# 1) Escribir un programa que me permita aplicar el 10% de descuento si la compra total es mayor a $100.

# In[6]:


def precio(cantidad):
    if(cantidad > 100):
        return cantidad*0.90
    else:
        return cantidad
    
precio(150)    


# 2) Sabiendo que la fórmula para obtener el área de un triángulo es a = (b x h) / 2, donde b es la longitud de la base del triángulo, y h es su altura. Escribir un programa que permita realizar el cálculo del área de un triángulo. Si el área contiene valores decimales, imprimir el resultado con dos dígitos. 

# In[8]:


def area(base, altura):
    print( "%.2f" % ((base*altura)/2))
    
area(10,15)   


# 3) La fórmula para el Índice de Masa Corportal es *IMC = kg/m2* donde kg es el peso de la persona en kilogramos y m2 es la altura en metros al cuadrado. Realizar un programa que calcula el IMC cuando se le provee el peso y la altura. 

# In[16]:


def IMC(peso, altura):
    return(peso/(altura**2))

IMC(75, 1.82)


# In[ ]:




