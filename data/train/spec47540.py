import numpy as np 

def function(x):

	e3 = 5
	x1 = x
	paths = []
	try:
		if x1 <= 2:
			x = x-2
			paths.append(1)
		else:
			x = x1+x
			x1 = 5+x1
			x1 = 3/8
			paths.append(2)
		if x >= 7:
			e3 = 4-e3
			x = 2*5
			paths.append(3)
		else:
			x1 = x+0
			x1 = 5+x1
			x1 = x*x1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))