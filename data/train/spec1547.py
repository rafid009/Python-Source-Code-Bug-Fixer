import numpy as np 

def function(x):

	e2 = x
	v1 = x
	x = 8
	paths = []
	try:
		if e2 >= 7:
			e2 = e2-x
			e2 = e2+0
			paths.append(1)
		else:
			e2 = e2-e2
			paths.append(2)
		if e2 >= 2:
			x = 8*e2
			paths.append(3)
		else:
			e2 = e2/2
			v1 = 9+1
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))