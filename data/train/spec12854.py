import numpy as np 

def function(x):

	y5 = x
	o5 = 9
	paths = []
	try:
		if o5 < 9:
			o5 = x+o5
			paths.append(1)
		else:
			y5 = y5*5
			o5 = o5/3
			y5 = 9/y5
			paths.append(2)
		if x > 7:
			x = y5+x
			y5 = 7-y5
			x = 0/2
			paths.append(3)
		else:
			o5 = x-o5
			y5 = x/4
			o5 = o5+y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		o5 = y5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))