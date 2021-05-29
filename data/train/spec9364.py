import numpy as np 

def function(x):

	e3 = 3
	m2 = 9
	paths = []
	try:
		if e3 > 7:
			e3 = e3/9
			x = x-e3
			e3 = e3+6
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x >= 7:
			e3 = e3-m2
			paths.append(3)
		else:
			x = x+4
			e3 = 1-1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))