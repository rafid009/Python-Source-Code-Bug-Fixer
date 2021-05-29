import numpy as np 

def function(x):

	o2 = x
	v4 = 4
	x = 3
	paths = []
	try:
		if v4 >= 8:
			x = x/1
			o2 = o2-4
			paths.append(1)
		else:
			x = x-8
			v4 = 4+v4
			o2 = 7-2
			paths.append(2)
		if x <= 3:
			v4 = 2-7
			v4 = o2-5
			paths.append(3)
		else:
			x = x+7
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))