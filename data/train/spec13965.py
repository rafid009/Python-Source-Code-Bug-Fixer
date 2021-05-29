import numpy as np 

def function(x):

	o4 = x
	a0 = 4
	paths = []
	try:
		if a0 >= 8:
			a0 = a0-1
			a0 = 9+x
			a0 = x/o4
			paths.append(1)
		else:
			x = x*o4
			a0 = 9*a0
			x = x*a0
			paths.append(2)
		if o4 <= 9:
			o4 = 7/o4
			a0 = 9-a0
			x = 2+1
			paths.append(3)
		else:
			o4 = 9-6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		a0 = o4**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))