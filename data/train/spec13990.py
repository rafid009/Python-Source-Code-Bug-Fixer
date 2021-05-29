import numpy as np 

def function(x):

	k3 = x
	w0 = 5
	paths = []
	try:
		if k3 <= 1:
			k3 = k3*9
			w0 = 2*w0
			paths.append(1)
		else:
			w0 = 1+7
			paths.append(2)
		if w0 > 4:
			k3 = k3*w0
			w0 = 8-w0
			w0 = w0-8
			paths.append(3)
		else:
			k3 = k3*k3
			k3 = 4+k3
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		k3 = w0**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))