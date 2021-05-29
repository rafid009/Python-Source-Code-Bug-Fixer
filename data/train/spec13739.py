import numpy as np 

def function(x):

	e2 = 2
	y7 = x
	paths = []
	try:
		if y7 > 6:
			e2 = e2*9
			x = x+x
			e2 = 8+1
			paths.append(1)
		else:
			y7 = y7+8
			x = 6+x
			y7 = 6-y7
			paths.append(2)
		if y7 <= 0:
			y7 = 8+4
			y7 = y7+4
			paths.append(3)
		else:
			e2 = x/e2
			y7 = y7*8
			y7 = 3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))