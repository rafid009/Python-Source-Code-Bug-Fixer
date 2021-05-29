import numpy as np 

def function(x):

	e6 = 6
	p1 = 1
	paths = []
	try:
		if x < 8:
			x = x+x
			p1 = 1-x
			paths.append(1)
		else:
			e6 = 7-e6
			p1 = p1+0
			paths.append(2)
		if x < 9:
			x = p1/p1
			x = x+x
			x = x-2
			paths.append(3)
		else:
			x = x*6
			e6 = 9*x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))