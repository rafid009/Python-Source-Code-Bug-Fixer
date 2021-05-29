import numpy as np 

def function(x):

	p7 = x
	y1 = 6
	paths = []
	try:
		if x <= 9:
			x = 0-x
			y1 = p7+y1
			x = x*x
			paths.append(1)
		else:
			p7 = 3*2
			x = 9-p7
			y1 = x+7
			paths.append(2)
		if x < 7:
			p7 = 1*2
			p7 = p7-3
			paths.append(3)
		else:
			x = 9*x
			x = 1-x
			p7 = 6*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))