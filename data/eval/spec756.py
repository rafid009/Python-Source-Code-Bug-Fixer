import numpy as np 

def function(x):

	b3 = 9
	e2 = 9
	paths = []
	try:
		if x > 6:
			b3 = b3/5
			e2 = e2*5
			paths.append(1)
		else:
			e2 = 9-x
			x = 2/x
			paths.append(2)
		if b3 <= 7:
			x = 1/x
			b3 = b3*8
			x = 7*e2
			paths.append(3)
		else:
			x = 1-x
			b3 = b3/x
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))