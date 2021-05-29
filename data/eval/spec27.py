import numpy as np 

def function(x):

	x0 = 9
	p4 = 1
	paths = []
	try:
		if x0 <= 5:
			x = 9+x
			paths.append(1)
		else:
			x0 = 3/x0
			p4 = 8-x
			paths.append(2)
		if x0 <= 9:
			x0 = 9+8
			x = x+9
			x0 = x0+p4
			paths.append(3)
		else:
			x = p4+x
			p4 = p4*0
			p4 = p4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))