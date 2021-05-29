import numpy as np 

def function(x):

	e9 = 7
	a4 = x
	x = x
	paths = []
	try:
		if x < 2:
			x = 4-x
			x = a4*x
			paths.append(1)
		else:
			e9 = e9*0
			e9 = e9*8
			e9 = e9-7
			paths.append(2)
		if a4 >= 4:
			x = x-e9
			x = x*7
			a4 = a4+9
			paths.append(3)
		else:
			a4 = 0+a4
			a4 = a4*8
			a4 = a4+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))