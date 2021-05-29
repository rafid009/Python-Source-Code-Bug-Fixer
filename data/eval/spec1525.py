import numpy as np 

def function(x):

	n1 = x
	o9 = x
	x = x
	paths = []
	try:
		if n1 >= 1:
			o9 = o9/o9
			o9 = 5-x
			paths.append(1)
		else:
			o9 = o9-n1
			paths.append(2)
		if o9 >= 2:
			x = x/x
			paths.append(3)
		else:
			x = 9/x
			x = 2*x
			o9 = o9/7
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))