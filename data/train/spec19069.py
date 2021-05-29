import numpy as np 

def function(x):

	f8 = 6
	o3 = 3
	paths = []
	try:
		if f8 < 2:
			o3 = 9*o3
			f8 = 5+f8
			paths.append(1)
		else:
			x = f8-x
			f8 = f8+4
			o3 = f8*2
			paths.append(2)
		if o3 <= 1:
			x = 1*o3
			paths.append(3)
		else:
			x = 1-4
			x = x/8
			f8 = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))