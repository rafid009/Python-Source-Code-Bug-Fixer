import numpy as np 

def function(x):

	r2 = 7
	o5 = 6
	paths = []
	try:
		if o5 < 5:
			x = x-2
			paths.append(1)
		else:
			x = 4*o5
			x = x/5
			o5 = x+5
			paths.append(2)
		if o5 >= 8:
			x = 0*8
			o5 = 0-9
			o5 = o5/6
			paths.append(3)
		else:
			o5 = 1-o5
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