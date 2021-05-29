import numpy as np 

def function(x):

	o8 = 2
	f4 = 6
	paths = []
	try:
		if x <= 5:
			x = 2/x
			f4 = f4*1
			paths.append(1)
		else:
			o8 = o8/5
			paths.append(2)
		if f4 <= 1:
			f4 = 3*x
			f4 = x+0
			paths.append(3)
		else:
			f4 = 3-x
			o8 = 8*1
			f4 = 9*f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		o8 = f4**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))