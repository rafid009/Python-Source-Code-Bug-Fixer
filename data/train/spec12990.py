import numpy as np 

def function(x):

	a7 = 2
	b1 = x
	paths = []
	try:
		if x < 7:
			x = 0/2
			x = 7-8
			b1 = x+4
			paths.append(1)
		else:
			x = x/x
			x = x/6
			a7 = a7/a7
			paths.append(2)
		if x < 5:
			a7 = x/a7
			b1 = b1+3
			b1 = b1+3
			paths.append(3)
		else:
			b1 = 2*b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))