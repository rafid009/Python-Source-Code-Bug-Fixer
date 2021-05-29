import numpy as np 

def function(x):

	i1 = x
	e4 = 7
	paths = []
	try:
		if e4 <= 8:
			i1 = 1-i1
			e4 = e4-4
			e4 = 1-e4
			paths.append(1)
		else:
			x = i1/9
			e4 = x*e4
			paths.append(2)
		if e4 >= 2:
			x = x/2
			paths.append(3)
		else:
			e4 = 6+e4
			e4 = e4-i1
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))