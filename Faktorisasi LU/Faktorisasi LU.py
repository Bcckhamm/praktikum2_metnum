print ()
print ()
print ()
print ("Nama : Beckham Silvester Pakpahan")
print ("Kelas :  TIF3A6")
print ("NPM : 202010225247")
print ()
print ()
print ()


import scipy
from scipy.linalg import lu, lu_factor, lu_solve
import numpy as np

# Definisikan matriks A
A = np.array([[3., -0.1, -0.2], [0.1, 7., -0.3], [0.3, -0.2, 10]])

# Definisikan vektor b
b = np.array([7.85, -19.3, 71.4])

# Solusi yang diberikan Lu dan b
P, L, U = lu(A)
lu, piv = lu_factor(A)
x = lu_solve((lu, piv),b)
print ('Matriks P :\n ',P)
print ('Matriks L :\n ',L)
print ('Matriks U :\n ',U)
print ('Solutions :\n ',x)