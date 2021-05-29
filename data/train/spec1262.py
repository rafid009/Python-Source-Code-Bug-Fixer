import numpy as np 

def function(x):

	e0 = x
	a5 = 7
	paths = []
	try:
		if x > 9:
			a5 = a5+e0
			paths.append(1)
		else:
			x = x-a5
			paths.append(2)
		if e0 <= 6:
			x = e0+x
			a5 = a5-a5
			x = e0/x
			paths.append(3)
		else:
			e0 = e0+0
			e0 = 6/e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))