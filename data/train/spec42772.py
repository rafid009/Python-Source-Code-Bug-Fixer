import numpy as np 

def function(x):

	n1 = 5
	o5 = x
	paths = []
	try:
		if x >= 3:
			n1 = 2*9
			n1 = n1-9
			paths.append(1)
		else:
			o5 = x+9
			n1 = n1*3
			paths.append(2)
		if x < 2:
			x = x-0
			o5 = n1+4
			paths.append(3)
		else:
			n1 = 9-o5
			o5 = 3+n1
			x = x-o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))