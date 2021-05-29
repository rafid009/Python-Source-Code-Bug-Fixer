import numpy as np 

def function(x):

	o5 = x
	y7 = x
	paths = []
	try:
		if x < 3:
			o5 = 5/o5
			paths.append(1)
		else:
			y7 = y7-4
			y7 = y7*4
			y7 = y7*o5
			paths.append(2)
		if x > 2:
			x = x/x
			x = x+y7
			paths.append(3)
		else:
			x = 1+9
			o5 = o5/y7
			o5 = o5*y7
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		o5 = y7**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))