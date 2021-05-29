import numpy as np 

def function(x):

	x6 = 1
	p6 = 4
	paths = []
	try:
		if x < 1:
			x6 = x6*3
			x = 8*x
			paths.append(1)
		else:
			p6 = 4*p6
			x6 = 1-x
			paths.append(2)
		if x6 < 2:
			p6 = p6+7
			x = x*5
			paths.append(3)
		else:
			p6 = 5+x
			x6 = x6*9
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))