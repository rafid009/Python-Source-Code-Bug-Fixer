import numpy as np 

def function(x):

	v3 = 1
	f8 = x
	paths = []
	try:
		if v3 >= 0:
			f8 = 8+f8
			paths.append(1)
		else:
			f8 = 0-f8
			f8 = f8-3
			paths.append(2)
		if x > 8:
			v3 = 8-2
			paths.append(3)
		else:
			f8 = f8*0
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