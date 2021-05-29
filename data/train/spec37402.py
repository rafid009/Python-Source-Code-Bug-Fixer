import numpy as np 

def function(x):

	g7 = 5
	e5 = 4
	paths = []
	try:
		if x >= 5:
			e5 = 3+0
			g7 = g7+6
			paths.append(1)
		else:
			e5 = 2*e5
			e5 = e5+6
			paths.append(2)
		if x > 4:
			e5 = e5-9
			paths.append(3)
		else:
			x = 5*0
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))