import numpy as np 

def function(x):

	n1 = x
	o5 = x
	paths = []
	try:
		if x >= 4:
			x = x-x
			n1 = 7-4
			n1 = 7*o5
			paths.append(1)
		else:
			n1 = o5+n1
			n1 = 7+n1
			paths.append(2)
		if x < 2:
			o5 = 7+o5
			paths.append(3)
		else:
			o5 = 5-o5
			n1 = n1+n1
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))