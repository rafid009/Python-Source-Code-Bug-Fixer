import numpy as np 

def function(x):

	y6 = 1
	p6 = 8
	paths = []
	try:
		if x >= 6:
			p6 = 5*p6
			x = x-6
			paths.append(1)
		else:
			y6 = 8+x
			y6 = y6+8
			y6 = y6/9
			paths.append(2)
		if x > 9:
			y6 = y6-8
			x = 1*x
			x = x+3
			paths.append(3)
		else:
			p6 = y6+p6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))