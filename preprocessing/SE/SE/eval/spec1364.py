import numpy as np 

def function(x):

	l6 = x
	e6 = 1
	paths = []
	try:
		if x < 1:
			x = x-7
			l6 = l6+l6
			e6 = e6/x
			paths.append(1)
		else:
			x = x+2
			e6 = 5-7
			paths.append(2)
		if l6 >= 0:
			l6 = 8+2
			x = 8-1
			e6 = e6*9
			paths.append(3)
		else:
			x = x-6
			x = 8*2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))