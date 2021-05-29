import numpy as np 

def function(x):

	o8 = 1
	v0 = 2
	paths = []
	try:
		if x <= 3:
			x = x-6
			paths.append(1)
		else:
			v0 = v0*4
			o8 = x*2
			v0 = v0+6
			paths.append(2)
		if x < 2:
			o8 = x+o8
			v0 = x/x
			paths.append(3)
		else:
			v0 = 6/v0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		v0 = o8**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))