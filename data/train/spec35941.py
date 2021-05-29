import numpy as np 

def function(x):

	o4 = x
	a4 = 1
	paths = []
	try:
		if o4 >= 2:
			x = 0+x
			x = 8+x
			paths.append(1)
		else:
			x = a4-7
			x = 7/8
			x = x+7
			paths.append(2)
		if o4 > 2:
			o4 = o4*o4
			a4 = a4-0
			paths.append(3)
		else:
			x = x+2
			o4 = x*o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		a4 = o4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))