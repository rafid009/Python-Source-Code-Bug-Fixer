import numpy as np 

def function(x):

	o5 = 7
	x2 = 1
	x = 4
	paths = []
	try:
		if x >= 3:
			x = 1+x
			o5 = x-o5
			x = x-9
			paths.append(1)
		else:
			o5 = x2/o5
			x2 = x*2
			o5 = 7+o5
			paths.append(2)
		if x2 >= 0:
			x2 = x2*9
			x2 = x2/o5
			paths.append(3)
		else:
			x = 3-o5
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