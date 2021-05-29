import numpy as np 

def function(x):

	v3 = 6
	o8 = x
	paths = []
	try:
		if x < 6:
			x = 9/o8
			paths.append(1)
		else:
			o8 = o8+x
			x = v3-v3
			paths.append(2)
		if v3 <= 1:
			o8 = 9*4
			v3 = 8-o8
			paths.append(3)
		else:
			o8 = o8*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))