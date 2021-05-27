import numpy as np 

def function(x):

	k3 = x
	w5 = 3
	paths = []
	try:
		if k3 < 3:
			w5 = w5+6
			x = 3/w5
			paths.append(1)
		else:
			k3 = k3/9
			x = x-5
			paths.append(2)
		if k3 < 8:
			k3 = k3*4
			w5 = x-w5
			x = k3/x
			paths.append(3)
		else:
			x = 1*x
			w5 = w5*8
			k3 = k3*5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		k3 = w5**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))