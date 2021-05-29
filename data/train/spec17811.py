import numpy as np 

def function(x):

	e2 = 3
	a1 = 9
	x = x
	paths = []
	try:
		if x < 9:
			e2 = e2/e2
			x = x+3
			x = x+9
			paths.append(1)
		else:
			e2 = 3-e2
			a1 = a1+a1
			paths.append(2)
		if e2 >= 1:
			x = 5+x
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))