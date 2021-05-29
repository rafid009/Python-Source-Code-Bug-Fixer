import numpy as np 

def function(x):

	o6 = 4
	l8 = 9
	paths = []
	try:
		if o6 < 0:
			l8 = l8-4
			o6 = o6-x
			paths.append(1)
		else:
			l8 = 3/2
			l8 = 3-l8
			x = x+1
			paths.append(2)
		if l8 > 8:
			o6 = 1-o6
			l8 = l8+1
			x = 2+o6
			paths.append(3)
		else:
			l8 = 0-8
			o6 = 3/3
			x = x*l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		o6 = l8**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))