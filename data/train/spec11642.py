import numpy as np 

def function(x):

	x5 = 5
	e1 = 0
	paths = []
	try:
		if x <= 0:
			e1 = e1*e1
			x5 = 8*2
			e1 = e1/x5
			paths.append(1)
		else:
			x5 = x5*0
			e1 = x5-9
			paths.append(2)
		if x >= 3:
			x = x-6
			e1 = e1-2
			x = 6+2
			paths.append(3)
		else:
			e1 = x5-7
			x = x+5
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))