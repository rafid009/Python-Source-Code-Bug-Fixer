import numpy as np 

def function(x):

	f8 = 1
	e8 = x
	paths = []
	try:
		if e8 >= 6:
			x = 7+f8
			e8 = e8/1
			paths.append(1)
		else:
			e8 = e8-2
			paths.append(2)
		if x < 1:
			f8 = f8+f8
			e8 = x/e8
			x = 3/6
			paths.append(3)
		else:
			x = 9*x
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