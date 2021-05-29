import numpy as np 

def function(x):

	o5 = 0
	p6 = 8
	paths = []
	try:
		if o5 <= 6:
			o5 = 1+x
			x = x/3
			p6 = p6-9
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if o5 <= 1:
			p6 = p6*6
			p6 = 2/p6
			x = 4-1
			paths.append(3)
		else:
			p6 = p6-x
			x = x-1
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