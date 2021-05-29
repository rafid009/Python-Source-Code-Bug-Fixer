import numpy as np 

def function(x):

	o7 = 0
	r3 = 1
	paths = []
	try:
		if o7 >= 8:
			o7 = x/o7
			o7 = x*x
			x = 7/x
			paths.append(1)
		else:
			r3 = 3+x
			o7 = 3-o7
			paths.append(2)
		if r3 > 9:
			x = r3-x
			paths.append(3)
		else:
			x = x*5
			x = 0*1
			x = x-5
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