import numpy as np 

def function(x):

	o8 = 3
	r7 = x
	paths = []
	try:
		if r7 < 1:
			r7 = 5-r7
			paths.append(1)
		else:
			x = o8-r7
			x = 4+o8
			x = 8+o8
			paths.append(2)
		if r7 < 7:
			r7 = r7/o8
			o8 = x+7
			o8 = 3+2
			paths.append(3)
		else:
			r7 = 0+r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))