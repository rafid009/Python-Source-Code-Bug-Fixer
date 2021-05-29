import numpy as np 

def function(x):

	o1 = 3
	o7 = 9
	x = x
	paths = []
	try:
		if x >= 5:
			o7 = o7-o7
			paths.append(1)
		else:
			x = x-8
			o1 = o1/o7
			o7 = 0-8
			paths.append(2)
		if x <= 4:
			o1 = o1/8
			o7 = o7/1
			o1 = 4/o1
			paths.append(3)
		else:
			x = x-1
			x = 9/x
			o7 = 5*x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o1 = o7**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))