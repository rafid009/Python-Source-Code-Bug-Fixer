import numpy as np 

def function(x):

	y7 = 1
	p6 = x
	paths = []
	try:
		if p6 >= 2:
			y7 = 0+y7
			y7 = y7+2
			y7 = y7+7
			paths.append(1)
		else:
			y7 = y7+3
			paths.append(2)
		if p6 < 2:
			y7 = y7-8
			x = x/7
			paths.append(3)
		else:
			p6 = p6/8
			x = x*7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		y7 = p6**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))