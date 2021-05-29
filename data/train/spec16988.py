import numpy as np 

def function(x):

	v1 = x
	p7 = 1
	paths = []
	try:
		if x >= 2:
			p7 = 4+0
			paths.append(1)
		else:
			p7 = 8+0
			p7 = p7*6
			p7 = p7+7
			paths.append(2)
		if p7 > 3:
			p7 = 1/p7
			x = 9*x
			v1 = v1+8
			paths.append(3)
		else:
			v1 = v1/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))