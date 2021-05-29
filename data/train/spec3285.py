import numpy as np 

def function(x):

	e6 = 9
	e8 = x
	x = 7
	paths = []
	try:
		if x >= 8:
			e6 = e8*1
			x = 8-x
			e6 = x+1
			paths.append(1)
		else:
			x = 7*3
			e6 = 3*x
			e8 = e8/1
			paths.append(2)
		if e8 < 9:
			e6 = 3*e6
			e6 = 1*3
			paths.append(3)
		else:
			x = x*7
			e6 = 6/6
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