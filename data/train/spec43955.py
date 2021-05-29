import numpy as np 

def function(x):

	o1 = 5
	o9 = x
	paths = []
	try:
		if o1 < 0:
			o9 = 9/o9
			paths.append(1)
		else:
			x = o9-3
			o9 = o9-4
			o9 = 8-o1
			paths.append(2)
		if o1 < 9:
			o9 = o9/7
			o9 = o9-9
			o1 = x-o1
			paths.append(3)
		else:
			o9 = 1*o9
			x = x-x
			o9 = 8-o9
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o9 = o1**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))