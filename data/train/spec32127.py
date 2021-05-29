import numpy as np 

def function(x):

	o4 = 4
	a8 = 7
	paths = []
	try:
		if a8 < 8:
			a8 = o4*a8
			a8 = a8-1
			a8 = a8-4
			paths.append(1)
		else:
			a8 = a8/a8
			o4 = o4/x
			x = x/1
			paths.append(2)
		if a8 >= 6:
			o4 = a8-0
			a8 = x*a8
			paths.append(3)
		else:
			x = o4*o4
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		o4 = a8**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))