import numpy as np 

def function(x):

	f0 = x
	o6 = x
	paths = []
	try:
		if o6 > 3:
			f0 = o6/f0
			f0 = f0*o6
			paths.append(1)
		else:
			f0 = 6/3
			paths.append(2)
		if o6 <= 4:
			o6 = f0+o6
			x = x/9
			o6 = x*4
			paths.append(3)
		else:
			x = x-7
			o6 = o6-9
			x = 6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))