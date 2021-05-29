import numpy as np 

def function(x):

	o9 = 9
	o2 = x
	paths = []
	try:
		if o9 < 3:
			o2 = o2/8
			o2 = 4/8
			paths.append(1)
		else:
			o2 = 9-7
			o9 = o9+2
			o2 = o2+o2
			paths.append(2)
		if o2 > 0:
			o9 = o9/1
			paths.append(3)
		else:
			o9 = o9-9
			x = x/8
			x = x+o9
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