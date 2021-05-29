import numpy as np 

def function(x):

	y1 = x
	e5 = x
	x = 7
	paths = []
	try:
		if y1 <= 9:
			y1 = y1/e5
			x = x*2
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if e5 >= 3:
			y1 = 1-9
			y1 = y1*2
			e5 = 9*2
			paths.append(3)
		else:
			x = 6/x
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