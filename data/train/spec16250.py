import numpy as np 

def function(x):

	e6 = x
	y3 = 5
	paths = []
	try:
		if y3 >= 4:
			y3 = 5*x
			y3 = 5/y3
			y3 = y3-2
			paths.append(1)
		else:
			e6 = x/9
			x = x*8
			x = 6*x
			paths.append(2)
		if y3 <= 9:
			y3 = x*y3
			x = x/8
			paths.append(3)
		else:
			e6 = 2-e6
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