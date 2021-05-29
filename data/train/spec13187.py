import numpy as np 

def function(x):

	k4 = x
	o7 = 9
	paths = []
	try:
		if x < 1:
			o7 = 0*o7
			o7 = 7-o7
			o7 = k4+6
			paths.append(1)
		else:
			k4 = x+6
			paths.append(2)
		if k4 <= 6:
			o7 = o7/3
			x = x*5
			paths.append(3)
		else:
			x = o7-0
			o7 = 0/o7
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))