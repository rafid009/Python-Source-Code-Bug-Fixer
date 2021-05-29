import numpy as np 

def function(x):

	r2 = x
	o8 = 2
	paths = []
	try:
		if r2 >= 4:
			o8 = x+5
			x = 9*x
			paths.append(1)
		else:
			x = 8*0
			r2 = 5/r2
			paths.append(2)
		if o8 >= 4:
			o8 = 1*o8
			paths.append(3)
		else:
			o8 = o8-7
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))