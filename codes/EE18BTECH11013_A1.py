import numpy as np
import matplotlib.pyplot as plt


def plot(L, Fn, St):
	for i in range(len(L)):
		s=0
		for j in range(len(L)):
			s=s + 	L[j]*np.exp((2*np.pi*i*j*(-c))/len(L))
		Fn[i]=s
		
	plt.grid()
	plt.xlabel("n"); plt.ylabel(" Absoulute " + str(St))
	plt.stem(n,np.absolute(Fn))
	plt.show()
	
	plt.grid()
	plt.xlabel("n"); plt.ylabel("Phase ang " + str(St))
	plt.stem(n,np.angle(Fn))
	plt.show()
		
#plot of X(n)
n=np.arange(6)
c=complex(0,1)
X=np.array([1,2,3,4,2,1])
Xn=np.zeros(len(X),dtype='complex')
plot(X,Xn,'X(n)')
		
#plot of H(n)
n=np.arange(15)
u1=np.ones(15)
u2=np.array([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
H=np.zeros(15)
s=0
for i in range(15):
    H[i]=((-0.5)**i)*u1[i] + ((-0.5)**(i-2))*u2[i]
Hn=np.zeros(len(H),dtype='complex')

plot(H, Hn,'H(n)')

for i in range(len(H)):
    s=0
    for j in range(len(H)):
        s=s+H[j]*np.exp((-c*2*np.pi*i*j)/len(H))
    Hn[i]=s


