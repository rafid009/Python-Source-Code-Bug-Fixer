import numpy as np 

def function(x):

	k3 = 5
	b7 = x
	paths = []
	try:
		if b7 > 4:
			k3 = k3-1
			x = 3-x
			x = x*1
			paths.append(1)
		else:
			k3 = x/x
			paths.append(2)
		if k3 <= 3:
			b7 = b7*x
			paths.append(3)
		else:
			b7 = b7*b7
			k3 = 6*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))