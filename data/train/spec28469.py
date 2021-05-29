import numpy as np 

def function(x):

	o8 = x
	u5 = 1
	paths = []
	try:
		if o8 > 0:
			o8 = u5*o8
			o8 = x-x
			paths.append(1)
		else:
			x = u5*x
			u5 = u5/x
			paths.append(2)
		if o8 <= 8:
			x = 9/x
			x = x+1
			o8 = x+6
			paths.append(3)
		else:
			u5 = u5/u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		o8 = u5**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))