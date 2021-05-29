import numpy as np 

def function(x):

	e2 = x
	i5 = 9
	paths = []
	try:
		if e2 > 1:
			e2 = 1*9
			x = x-e2
			e2 = e2*2
			paths.append(1)
		else:
			i5 = x/i5
			paths.append(2)
		if x < 8:
			i5 = 9/i5
			paths.append(3)
		else:
			i5 = 5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))