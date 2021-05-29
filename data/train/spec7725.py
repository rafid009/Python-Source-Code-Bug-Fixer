import numpy as np 

def function(x):

	x0 = x
	p2 = 4
	paths = []
	try:
		if x0 >= 2:
			p2 = p2*0
			x0 = p2-p2
			paths.append(1)
		else:
			p2 = 9+p2
			paths.append(2)
		if x < 6:
			x = x-x0
			paths.append(3)
		else:
			x0 = 6+p2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))