import numpy as np 

def function(x):

	f2 = 0
	e8 = x
	paths = []
	try:
		if f2 <= 8:
			x = 0*x
			x = x/6
			paths.append(1)
		else:
			f2 = 9*f2
			paths.append(2)
		if e8 <= 0:
			x = 7-x
			paths.append(3)
		else:
			e8 = e8-6
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