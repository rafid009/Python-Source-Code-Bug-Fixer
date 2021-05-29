import numpy as np 

def function(x):

	o5 = x
	n9 = x
	x = 0
	paths = []
	try:
		if n9 < 5:
			n9 = n9-0
			x = x/o5
			o5 = 4+n9
			paths.append(1)
		else:
			o5 = o5/o5
			o5 = o5*9
			paths.append(2)
		if x >= 7:
			x = 3*x
			x = 9*x
			x = 8*7
			paths.append(3)
		else:
			n9 = 6-2
			n9 = 7/3
			o5 = 7+o5
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