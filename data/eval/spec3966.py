import numpy as np 

def function(x):

	e4 = x
	x6 = 3
	paths = []
	try:
		if e4 > 7:
			e4 = e4*9
			paths.append(1)
		else:
			x = x+7
			x6 = x6-8
			paths.append(2)
		if e4 <= 2:
			e4 = 8*e4
			x = x/1
			paths.append(3)
		else:
			e4 = e4*e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))