import numpy as np 

def function(x):

	o1 = 6
	o4 = x
	paths = []
	try:
		if o1 > 9:
			o1 = o1*1
			o4 = 3+5
			paths.append(1)
		else:
			o1 = 3+8
			x = 3+x
			paths.append(2)
		if o1 > 7:
			x = 2-o1
			x = x/4
			paths.append(3)
		else:
			o4 = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))