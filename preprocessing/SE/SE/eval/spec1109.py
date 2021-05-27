import numpy as np 

def function(x):

	f4 = 3
	o3 = 5
	paths = []
	try:
		if f4 < 2:
			f4 = f4/2
			f4 = o3/9
			paths.append(1)
		else:
			f4 = 7+f4
			paths.append(2)
		if x < 8:
			o3 = o3+3
			paths.append(3)
		else:
			x = 5/x
			f4 = x/f4
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