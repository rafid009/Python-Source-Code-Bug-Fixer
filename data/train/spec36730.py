import numpy as np 

def function(x):

	o7 = x
	n5 = x
	paths = []
	try:
		if o7 < 0:
			x = x-o7
			x = 7*x
			o7 = o7-4
			paths.append(1)
		else:
			x = 2-1
			paths.append(2)
		if n5 > 3:
			n5 = n5/2
			x = x-5
			paths.append(3)
		else:
			n5 = 1/n5
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		n5 = o7**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))