import numpy as np 

def function(x):

	b3 = x
	e8 = 0
	paths = []
	try:
		if x <= 2:
			x = e8/8
			paths.append(1)
		else:
			b3 = x+0
			paths.append(2)
		if e8 < 3:
			x = x+2
			x = 9*x
			paths.append(3)
		else:
			e8 = e8-e8
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		e8 = b3**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))