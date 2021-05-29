import numpy as np 

def function(x):

	w8 = 8
	n6 = x
	paths = []
	try:
		if n6 >= 9:
			x = x-x
			n6 = n6/3
			x = x+w8
			paths.append(1)
		else:
			x = n6+7
			w8 = w8/x
			paths.append(2)
		if x >= 7:
			x = 8/8
			x = 1/1
			x = x-8
			paths.append(3)
		else:
			n6 = x-4
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))