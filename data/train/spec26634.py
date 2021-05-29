import numpy as np 

def function(x):

	o6 = x
	r6 = 0
	paths = []
	try:
		if o6 > 9:
			x = o6/4
			x = 5/x
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if r6 >= 3:
			x = o6/x
			x = 6-x
			o6 = 2/o6
			paths.append(3)
		else:
			x = 7+7
			o6 = o6*6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))