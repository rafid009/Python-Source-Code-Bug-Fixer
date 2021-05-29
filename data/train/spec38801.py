import numpy as np 

def function(x):

	x5 = 3
	o7 = x
	paths = []
	try:
		if x5 > 1:
			x5 = x*x5
			paths.append(1)
		else:
			o7 = 8+7
			paths.append(2)
		if o7 > 6:
			o7 = o7*x
			o7 = o7+2
			x = x-6
			paths.append(3)
		else:
			o7 = o7*1
			o7 = o7+1
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		o7 = x5**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))