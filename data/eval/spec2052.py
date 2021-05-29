import numpy as np 

def function(x):

	n6 = x
	o1 = 1
	paths = []
	try:
		if n6 <= 8:
			x = 0-o1
			x = 4+o1
			o1 = o1-7
			paths.append(1)
		else:
			n6 = n6/5
			paths.append(2)
		if n6 < 0:
			o1 = 2+8
			n6 = o1/n6
			paths.append(3)
		else:
			x = x/7
			o1 = o1*x
			n6 = n6*6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		o1 = n6**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))