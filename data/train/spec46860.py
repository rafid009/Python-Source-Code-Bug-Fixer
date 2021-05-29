import numpy as np 

def function(x):

	n1 = x
	o9 = x
	paths = []
	try:
		if x < 3:
			x = x-5
			paths.append(1)
		else:
			o9 = o9*3
			x = 1*x
			paths.append(2)
		if o9 < 0:
			n1 = 6+o9
			x = 8/8
			paths.append(3)
		else:
			n1 = o9+5
			o9 = o9/9
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