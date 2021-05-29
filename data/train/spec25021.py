import numpy as np 

def function(x):

	l0 = x
	o7 = 9
	paths = []
	try:
		if o7 >= 7:
			x = 1+6
			o7 = 4-x
			paths.append(1)
		else:
			o7 = o7*0
			x = 5+x
			paths.append(2)
		if x <= 9:
			o7 = o7/2
			o7 = x-4
			x = o7-x
			paths.append(3)
		else:
			l0 = 7+l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))