import numpy as np 

def function(x):

	f8 = 6
	o1 = x
	paths = []
	try:
		if o1 < 1:
			f8 = f8/8
			x = x*5
			x = x*8
			paths.append(1)
		else:
			o1 = o1*4
			o1 = o1/5
			f8 = f8/o1
			paths.append(2)
		if f8 >= 3:
			f8 = 5+7
			o1 = 1+o1
			f8 = 3/f8
			paths.append(3)
		else:
			x = 7/x
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