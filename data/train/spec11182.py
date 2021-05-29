import numpy as np 

def function(x):

	o6 = 2
	x0 = 1
	paths = []
	try:
		if x0 <= 8:
			o6 = 0/o6
			x = x/1
			x0 = x+2
			paths.append(1)
		else:
			x = x+7
			x0 = x0/6
			paths.append(2)
		if o6 >= 1:
			x = 7+5
			o6 = x0+o6
			paths.append(3)
		else:
			x = x0-x
			x = x+x0
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		o6 = x0**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))