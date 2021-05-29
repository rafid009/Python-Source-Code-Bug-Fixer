import numpy as np 

def function(x):

	p7 = x
	i0 = x
	paths = []
	try:
		if p7 <= 5:
			x = 6*x
			p7 = p7/1
			paths.append(1)
		else:
			p7 = x*9
			paths.append(2)
		if p7 > 6:
			p7 = x-x
			paths.append(3)
		else:
			x = 4*x
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