import numpy as np 

def function(x):

	p7 = 7
	y8 = x
	paths = []
	try:
		if y8 <= 1:
			y8 = 8/y8
			paths.append(1)
		else:
			p7 = 9+p7
			x = x-6
			paths.append(2)
		if y8 > 9:
			y8 = 4*y8
			p7 = 2+8
			paths.append(3)
		else:
			x = 0+x
			y8 = x*9
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