import numpy as np 

def function(x):

	e3 = x
	y3 = 2
	paths = []
	try:
		if y3 >= 2:
			y3 = y3/5
			paths.append(1)
		else:
			e3 = e3-6
			x = 8/2
			paths.append(2)
		if x > 9:
			e3 = x*7
			y3 = y3+1
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))