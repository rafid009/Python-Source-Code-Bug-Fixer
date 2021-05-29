import numpy as np 

def function(x):

	d4 = x
	o5 = 5
	paths = []
	try:
		if d4 <= 3:
			x = o5+x
			paths.append(1)
		else:
			d4 = 6+d4
			paths.append(2)
		if x <= 6:
			o5 = 0/7
			paths.append(3)
		else:
			x = 3-x
			o5 = o5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))