import numpy as np 

def function(x):

	y6 = x
	p7 = x
	paths = []
	try:
		if p7 <= 6:
			y6 = 8*y6
			paths.append(1)
		else:
			x = x/x
			y6 = p7*4
			p7 = 1-p7
			paths.append(2)
		if y6 < 1:
			p7 = 3*p7
			paths.append(3)
		else:
			p7 = 0+8
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))