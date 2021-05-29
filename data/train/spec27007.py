import numpy as np 

def function(x):

	x7 = 7
	e3 = 4
	paths = []
	try:
		if e3 < 5:
			e3 = x7+1
			e3 = 4-e3
			paths.append(1)
		else:
			x = x7*x7
			paths.append(2)
		if x7 < 1:
			e3 = x-5
			paths.append(3)
		else:
			x = 4/e3
			x = 1/8
			x7 = x7-7
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