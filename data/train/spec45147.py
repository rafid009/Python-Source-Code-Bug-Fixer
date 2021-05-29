import numpy as np 

def function(x):

	p0 = 5
	x3 = x
	x = 3
	paths = []
	try:
		if x < 1:
			x = x+p0
			paths.append(1)
		else:
			x = x/7
			p0 = p0-x3
			p0 = 6/p0
			paths.append(2)
		if p0 >= 9:
			x = p0-3
			p0 = 8-x3
			x3 = 5/2
			paths.append(3)
		else:
			x = x+9
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x3 = p0**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))