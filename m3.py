import cv2
import numpy as np

original = cv2.imread('carro3.jpg')
imagem2 = cv2.imread('carro4.jpg')
gray_original = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gray_imagem2 = cv2.cvtColor(imagem2,cv2.COLOR_BGR2GRAY)
_, escala = cv2.threshold(gray_original,127,255,cv2.THRESH_BINARY)

imgres = np.zeros(gray_original.shape,np.uint8)
imdilat = np.zeros([escala.shape[0],escala.shape[1]], dtype=np.uint8)
imerosao = np.zeros([escala.shape[0],escala.shape[1]], dtype=np.uint8)
opening = np.zeros([escala.shape[0],escala.shape[1]], dtype=np.uint8)
closed = np.zeros([escala.shape[0],escala.shape[1]], dtype=np.uint8)
mascres = np.zeros([gray_imagem2[0],escala.shape[1]], dtype=np.uint8)
mascarar = np.zeros([gray_imagem2[0],escala.shape[1]], dtype=np.uint8)


for x in range(gray_original.shape[0] - 1):
    for y in range(gray_original.shape[1] - 1):
        #Pontos Salientes
        r1 = -1*(gray_original[x-1,y-1])
        r2 = -1*(gray_original[x,y-1])
        r3 = -1*(gray_original[x+1,y-1])
        r4 = -1*(gray_original[x-1,y])
        r5 = 8*(gray_original[x,y])
        r6 = -1*(gray_original[x+1,y])
        r7 = -1*(gray_original[x-1,y+1])
        r8 = -1*(gray_original[x,y+1])
        r9 = -1*(gray_original[x+1,y+1])
        res =  r1+r2+r3+r4+r5+r6+r7+r8+r9
        imgres[x,y] = res

for x in range(escala.shape[0], escala.shape[1] -1):
	for y in range(escala.shape[0], escala.shape[1] -1):
		#Dilatacao
		if escala[x, y] != 0:
			imdilat[x-1, y-1] = escala[x, y]
			imdilat[x, y-1] = escala[x, y]
			imdilat[x+1, y-1] = escala[x, y]
			imdilat[x-1, y] = escala[x, y]
			imdilat[x, y] = escala[x, y]
			imdilat[x+1, y] = escala[x, y]
			imdilat[x-1, y+1] = escala[x, y]
			imdilat[x, y+1] = escala[x, y]
			imdilat[x+1, y+1] = escala[x, y]

# erosao navegar em posicao dentro da matriz [w] = largura, [h] = altura
#Erosao


for x in range(escala.shape[0] -1):
    for y in range (escala.shape[1] -1):
        if (imerosao[x-1,y-1] != 0) and (imerosao[x, y-1] != 0) and (imerosao[x+1,y-1] != 0) and (imerosao[x-1,y]!= 0) and(imerosao[x-1,y]!=0) and (imerosao[x,y]!=0) and (imerosao[x+1,y]!=0) and (imerosao[x-1,y+1]!=0) and (imerosao[x,y+1]!=0) and (imerosao[x+1,y+1]!=0):
            imerosao[x, y] = 255
        #aplicando Dilatacao em cima do result da erosao = opening
        if imerosao[x,y] != 0:
            opening[x-1,y-1] = escala[x,y]
            opening[x,y-1] = escala[x,y]
            opening[x+1,y-1] = escala[x,y]
            opening[x-1,y] = escala[x,y]
            opening[x,y] = escala[x,y]
            opening[x+1,y] = escala[x,y]
            opening[x-1,y+1] = escala[x,y]
            opening[x,y+1] = escala[x,y]
            opening[x+1,y+1] = escala[x,y]

    #Aplicando Erosao em cima da Dilatacao = fechamento, apartir do result da dilatacao da escala[x,y]

for x in range (escala.shape[0] -1):
    for y in range (escala.shape[1] -1):
        if ((imdilat[x-1,y-1]!=0) and
            (imdilat[x,y-1]) and
            (imdilat[x+1,y-1]!=0) and
            (imdilat[x-1,y]!=0) and
            (imdilat[x,y]!=0) and
            (imdilat[x+1,y]!=0) and
            (imdilat[x-1,y+1]!=0) and
            (imdilat[x,y+1]!=0) and
            (imdilat[x+1,y+1]!=0)):

            closed[i-1,j-1] = escala[x,y]
            closed[i,j-1] = escala[x,y]
            closed[i+1,j-1] = escala[x,y]
            closed[i-1,j] = escala[x,y]
            closed[i,j] = escala[x,y]
            closed[i+1,j] = escala[x,y]
            closed[i-1,j+1] = escala[x,y]
            closed[i,j+1] = escala[x,y]
            closed[i+1,j+1] = escala[x,y]

# Sobel
for x in range(gray_imagem2[0] -1):
	for y in range(gray_imagem2[1] -1):
		s1= -1*gray_imagem2[i-1,j-1]
		s2= -2*gray_imagem2[i-1,j]
		s3= -1*gray_imagem2[i-1,j+1]
		s4= 0*gray_imagem2[i,j-1]
		s5= 0*gray_imagem2[i,j]
		s6= 0*gray_imagem2[i,j+1]
		s7= 1*gray_imagem2[i+1,j-1]
		s8= 2*gray_imagem2[i+1,j]
		s9= 1*gray_imagem2[i+1,j+1]

		mascaras1 = (s7+2*s8+s9)-(s1+2*s2+s3)
		mascaras2 = (s3+2*s6+s9)-(s1+2*s4+s7)

#todos os valores de coluna
        mascres = mascara1+mascara2
#Roberts
"""
for
		rx1 = 0*gray_imagem2[i,j-1]
		rx2 = -1*gray_imagem2[i,j-1]
		rx3 = 1*gray_imagem2[i-1,j-1]
		rx4 = 0*gray_imagem2[]
		ry5 = 1*gray_imagem2[i+1,j-1]
		ry6 = 0*gray_imagem2[i-1,j-]
		ry7 = 0*gray_imagem2[]
		ry8 = -1*gray_imagem2[]

		pixelv = rx1+rx2+rx3+rx4
		pixelh = ry5+ry6+ry7+ry8

		g = sqrt(pixelv+pixelh)**2
		if g >pixelv or pixelh
		rbs = 255
#Robinson
"""
cv2.imshow('original', original)
cv2.imshow('deteccao',imgres)
cv2.imshow('dilatacao', imdilat)
cv2.imshow('erosao', imerosao)
cv2.imshow('opening', opening)
cv2.imshow('fechamento', closed)


cv2.waitKey(0)

