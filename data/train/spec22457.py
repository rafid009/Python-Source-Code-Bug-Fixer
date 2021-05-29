import numpy as np 

def function(x):

	p3 = 4
	p0 = x
	paths = []
	try:
		if x >= 0:
			x = 2/x
			x = x+p3
			p3 = 7+p3
			paths.append(1)
		else:
			p0 = p0*6
			p3 = 8+p0
			paths.append(2)
		if p0 <= 9:
			p0 = 9*5
			paths.append(3)
		else:
			p3 = p3/5
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))