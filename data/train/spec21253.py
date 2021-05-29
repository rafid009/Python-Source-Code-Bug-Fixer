import numpy as np 

def function(x):

	f1 = 3
	p7 = x
	paths = []
	try:
		if p7 < 1:
			x = 9*x
			paths.append(1)
		else:
			f1 = f1/p7
			f1 = f1/p7
			f1 = 9/f1
			paths.append(2)
		if f1 < 7:
			f1 = 1+f1
			x = x+p7
			paths.append(3)
		else:
			p7 = p7/f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))