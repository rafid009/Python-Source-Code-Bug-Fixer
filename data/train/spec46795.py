import numpy as np 

def function(x):

	v6 = 1
	o8 = 9
	paths = []
	try:
		if v6 >= 6:
			x = x-1
			o8 = o8/6
			o8 = o8-8
			paths.append(1)
		else:
			o8 = o8*3
			v6 = 5/2
			o8 = 2+v6
			paths.append(2)
		if x >= 4:
			o8 = 4+o8
			v6 = 6-x
			paths.append(3)
		else:
			o8 = o8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))