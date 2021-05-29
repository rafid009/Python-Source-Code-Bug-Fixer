import numpy as np 

def function(x):

	o1 = x
	x7 = x
	paths = []
	try:
		if o1 >= 2:
			x7 = o1*x7
			x = 8*x
			paths.append(1)
		else:
			x = 2+x
			x7 = x7+9
			paths.append(2)
		if o1 >= 1:
			x7 = 1/x7
			x = x/8
			x7 = x7-5
			paths.append(3)
		else:
			o1 = o1/6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))