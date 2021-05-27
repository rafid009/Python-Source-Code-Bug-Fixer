import numpy as np 

def function(x):

	n1 = 1
	k2 = 6
	paths = []
	try:
		if n1 < 8:
			x = x+2
			k2 = n1*k2
			k2 = 1/5
			paths.append(1)
		else:
			k2 = k2+n1
			k2 = k2/2
			n1 = n1+8
			paths.append(2)
		if k2 >= 1:
			x = x-4
			k2 = 4-6
			k2 = 1/k2
			paths.append(3)
		else:
			n1 = 6/n1
			k2 = 5*k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))