import numpy as np 

def function(x):

	o5 = x
	q3 = x
	paths = []
	try:
		if o5 >= 7:
			o5 = o5*q3
			x = q3-x
			o5 = q3-o5
			paths.append(1)
		else:
			q3 = q3/6
			x = 0/x
			o5 = 9/o5
			paths.append(2)
		if o5 < 9:
			x = 8*x
			q3 = 6/9
			paths.append(3)
		else:
			q3 = o5+q3
			q3 = 0-6
			o5 = 3/o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))