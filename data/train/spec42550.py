import numpy as np 

def function(x):

	o4 = x
	f5 = 5
	paths = []
	try:
		if f5 > 2:
			f5 = 9/f5
			paths.append(1)
		else:
			x = x+9
			f5 = f5+f5
			paths.append(2)
		if f5 > 3:
			o4 = o4/4
			paths.append(3)
		else:
			x = x-1
			f5 = f5/x
			o4 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))