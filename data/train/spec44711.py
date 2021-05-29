import numpy as np 

def function(x):

	o1 = 1
	p6 = x
	paths = []
	try:
		if o1 > 4:
			x = 8+8
			p6 = 8*p6
			paths.append(1)
		else:
			p6 = x+p6
			paths.append(2)
		if x < 0:
			p6 = 9*p6
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))