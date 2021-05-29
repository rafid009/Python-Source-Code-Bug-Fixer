import numpy as np 

def function(x):

	x8 = x
	p1 = x
	paths = []
	try:
		if p1 > 3:
			p1 = p1/5
			x8 = 2/x8
			paths.append(1)
		else:
			x = 2-x
			x8 = 2-x8
			paths.append(2)
		if p1 < 9:
			x8 = 4+x8
			x8 = p1*p1
			paths.append(3)
		else:
			x8 = 3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))