import numpy as np 

def function(x):

	o9 = x
	v5 = 2
	paths = []
	try:
		if o9 < 2:
			x = x*6
			v5 = v5+7
			x = x-3
			paths.append(1)
		else:
			v5 = 7-v5
			x = 0-x
			paths.append(2)
		if o9 >= 0:
			v5 = 9-3
			v5 = 3+o9
			paths.append(3)
		else:
			o9 = 3/x
			x = x/6
			o9 = o9*3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))