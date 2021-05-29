import numpy as np 

def function(x):

	f9 = x
	e7 = x
	paths = []
	try:
		if f9 <= 8:
			e7 = e7*1
			x = e7-x
			paths.append(1)
		else:
			f9 = f9+6
			e7 = 6-e7
			paths.append(2)
		if e7 <= 8:
			e7 = e7/e7
			x = 8*6
			f9 = 6*f9
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		e7 = f9**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))