import numpy as np 

def function(x):

	o5 = 6
	a0 = x
	paths = []
	try:
		if o5 >= 2:
			a0 = 7/a0
			o5 = o5*o5
			a0 = 7*a0
			paths.append(1)
		else:
			a0 = 2*x
			paths.append(2)
		if x > 8:
			a0 = a0*7
			o5 = 7/o5
			paths.append(3)
		else:
			o5 = o5+a0
			o5 = o5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))