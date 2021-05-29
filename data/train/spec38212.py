import numpy as np 

def function(x):

	o7 = x
	a6 = 2
	paths = []
	try:
		if o7 >= 2:
			a6 = 8+a6
			paths.append(1)
		else:
			a6 = o7+a6
			x = x-a6
			paths.append(2)
		if o7 <= 6:
			o7 = 3-a6
			a6 = a6-2
			paths.append(3)
		else:
			o7 = x-5
			o7 = 3/5
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		o7 = a6**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))