import numpy as np 

def function(x):

	e8 = x
	l4 = x
	paths = []
	try:
		if e8 <= 8:
			l4 = l4*6
			e8 = l4*9
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if e8 <= 5:
			x = x*6
			l4 = l4/x
			paths.append(3)
		else:
			e8 = e8/e8
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