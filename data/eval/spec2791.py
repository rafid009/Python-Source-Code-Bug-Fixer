import numpy as np 

def function(x):

	u4 = 9
	p6 = 4
	paths = []
	try:
		if p6 > 0:
			p6 = p6+7
			p6 = 9-p6
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if x <= 6:
			p6 = 0+3
			x = 8*x
			p6 = p6*u4
			paths.append(3)
		else:
			u4 = 9*u4
			x = 4*x
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