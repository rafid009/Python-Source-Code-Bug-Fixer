import numpy as np 

def function(x):

	p7 = 9
	y8 = x
	paths = []
	try:
		if y8 < 4:
			y8 = y8-6
			y8 = y8*5
			paths.append(1)
		else:
			y8 = y8*y8
			paths.append(2)
		if y8 < 8:
			p7 = 7-5
			y8 = 2+y8
			y8 = 6*p7
			paths.append(3)
		else:
			p7 = 8-p7
			x = x-x
			x = p7-0
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		y8 = p7**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))