import numpy as np 

def function(x):

	f1 = 9
	o7 = x
	paths = []
	try:
		if o7 > 7:
			o7 = o7-x
			o7 = 5-x
			o7 = 0*o7
			paths.append(1)
		else:
			x = 0/f1
			f1 = f1+f1
			f1 = 5+4
			paths.append(2)
		if o7 >= 3:
			o7 = 9+o7
			o7 = 9-2
			paths.append(3)
		else:
			f1 = 1/f1
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))