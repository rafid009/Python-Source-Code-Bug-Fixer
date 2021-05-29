import numpy as np 

def function(x):

	e5 = 6
	o7 = x
	paths = []
	try:
		if o7 >= 3:
			x = 6+x
			e5 = 0*e5
			paths.append(1)
		else:
			e5 = e5*3
			e5 = 7+3
			o7 = 5/8
			paths.append(2)
		if x >= 5:
			o7 = 5-o7
			e5 = e5/1
			o7 = o7/x
			paths.append(3)
		else:
			o7 = o7-6
			o7 = 2-o7
			o7 = o7*8
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