import numpy as np 

def function(x):

	x4 = 8
	p7 = x
	paths = []
	try:
		if p7 < 7:
			x = x/3
			x = x*9
			paths.append(1)
		else:
			x4 = x*5
			x = 1/8
			paths.append(2)
		if x4 > 0:
			p7 = x4-4
			p7 = 7*4
			paths.append(3)
		else:
			p7 = p7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))