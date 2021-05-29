import numpy as np 

def function(x):

	b6 = x
	e2 = 5
	paths = []
	try:
		if e2 < 2:
			x = 2*x
			e2 = b6/e2
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if e2 >= 2:
			x = x*e2
			e2 = x/b6
			paths.append(3)
		else:
			b6 = x+b6
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