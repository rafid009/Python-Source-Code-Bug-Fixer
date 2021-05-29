import numpy as np 

def function(x):

	e8 = x
	e6 = 7
	paths = []
	try:
		if e6 < 7:
			e8 = 9/2
			paths.append(1)
		else:
			e6 = e6-2
			x = e6/x
			paths.append(2)
		if e8 <= 9:
			x = x-x
			paths.append(3)
		else:
			x = e6/x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))