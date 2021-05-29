import numpy as np 

def function(x):

	o8 = 3
	n6 = x
	paths = []
	try:
		if n6 <= 2:
			n6 = n6+1
			o8 = n6/o8
			paths.append(1)
		else:
			x = o8/x
			o8 = o8+o8
			o8 = 0/2
			paths.append(2)
		if o8 <= 5:
			n6 = o8-9
			paths.append(3)
		else:
			o8 = 8/o8
			x = 6-7
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		o8 = n6**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))