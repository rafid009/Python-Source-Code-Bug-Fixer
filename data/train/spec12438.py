import numpy as np 

def function(x):

	o9 = x
	o7 = x
	paths = []
	try:
		if o7 < 4:
			o9 = 1+o9
			o7 = 4/o7
			o7 = 7/3
			paths.append(1)
		else:
			o9 = 0*x
			o7 = 5-o7
			o9 = o7-x
			paths.append(2)
		if o9 >= 6:
			x = x*4
			o9 = 3/4
			paths.append(3)
		else:
			x = x/1
			x = x-6
			o9 = 5+o9
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