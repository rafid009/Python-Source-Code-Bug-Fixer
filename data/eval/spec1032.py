import numpy as np 

def function(x):

	p2 = x
	d4 = 6
	paths = []
	try:
		if x >= 5:
			p2 = p2-6
			paths.append(1)
		else:
			p2 = 0+p2
			paths.append(2)
		if x > 1:
			d4 = 5-d4
			x = 1-x
			paths.append(3)
		else:
			x = 3*9
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))