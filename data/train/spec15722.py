import numpy as np 

def function(x):

	n6 = x
	o5 = x
	paths = []
	try:
		if n6 >= 3:
			x = x/x
			paths.append(1)
		else:
			o5 = o5*4
			o5 = 9/o5
			paths.append(2)
		if x <= 0:
			o5 = o5*9
			paths.append(3)
		else:
			n6 = n6-o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		n6 = o5**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))