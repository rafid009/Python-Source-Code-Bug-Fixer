import numpy as np 

def function(x):

	e5 = 9
	e4 = x
	paths = []
	try:
		if e5 > 2:
			e5 = 8+x
			e5 = e4+2
			x = x-0
			paths.append(1)
		else:
			x = 5/3
			x = 5*0
			paths.append(2)
		if x >= 1:
			e4 = e4-1
			x = e4+7
			e4 = 2*e4
			paths.append(3)
		else:
			e5 = 7*2
			e5 = e5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))