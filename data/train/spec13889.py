import numpy as np 

def function(x):

	p8 = x
	a9 = x
	paths = []
	try:
		if x <= 4:
			x = 6+p8
			paths.append(1)
		else:
			a9 = 2/a9
			paths.append(2)
		if x >= 4:
			a9 = 5*a9
			paths.append(3)
		else:
			x = x/p8
			p8 = 7/2
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))