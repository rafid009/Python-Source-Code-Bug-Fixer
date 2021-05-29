import numpy as np 

def function(x):

	o2 = 3
	e5 = 6
	paths = []
	try:
		if x >= 0:
			e5 = 5*2
			e5 = e5/8
			paths.append(1)
		else:
			e5 = 6-o2
			x = x*2
			o2 = o2/5
			paths.append(2)
		if e5 > 9:
			o2 = e5*e5
			paths.append(3)
		else:
			o2 = 0-o2
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))