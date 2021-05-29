import numpy as np 

def function(x):

	b6 = x
	e0 = x
	x = 7
	paths = []
	try:
		if e0 < 7:
			x = b6*8
			x = 4*x
			paths.append(1)
		else:
			b6 = b6+5
			x = 4/x
			x = e0/b6
			paths.append(2)
		if x >= 7:
			e0 = e0/3
			x = x/3
			e0 = e0/3
			paths.append(3)
		else:
			b6 = b6/3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))