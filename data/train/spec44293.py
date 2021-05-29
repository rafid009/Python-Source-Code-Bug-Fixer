import numpy as np 

def function(x):

	e2 = 5
	e9 = 6
	paths = []
	try:
		if e9 <= 6:
			x = x/e2
			e9 = 7-x
			e2 = e2+e2
			paths.append(1)
		else:
			x = x*3
			x = x*6
			e2 = e2*7
			paths.append(2)
		if x > 0:
			x = 4+x
			e9 = 1+7
			paths.append(3)
		else:
			e2 = e2+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))