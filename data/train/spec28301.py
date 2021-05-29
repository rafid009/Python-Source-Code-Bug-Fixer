import numpy as np 

def function(x):

	e1 = 1
	c8 = x
	paths = []
	try:
		if e1 <= 4:
			e1 = e1*5
			x = e1/x
			x = x-5
			paths.append(1)
		else:
			e1 = e1/3
			paths.append(2)
		if e1 < 4:
			x = x*x
			x = x+5
			paths.append(3)
		else:
			e1 = 3+e1
			e1 = c8*e1
			e1 = 3/e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))