import numpy as np 

def function(x):

	o4 = x
	f5 = 3
	x = x
	paths = []
	try:
		if o4 < 8:
			f5 = x+8
			paths.append(1)
		else:
			o4 = o4+5
			x = 6*x
			x = x-7
			paths.append(2)
		if o4 > 2:
			o4 = 2-2
			paths.append(3)
		else:
			f5 = 7*f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		o4 = f5**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))