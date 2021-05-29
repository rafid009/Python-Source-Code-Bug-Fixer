import numpy as np 

def function(x):

	o0 = x
	x0 = 9
	paths = []
	try:
		if x >= 5:
			o0 = x0*o0
			o0 = 8+o0
			o0 = 7+4
			paths.append(1)
		else:
			x = x*x
			o0 = 2+x
			o0 = 4-x
			paths.append(2)
		if x <= 6:
			o0 = o0+x0
			x0 = o0+x0
			paths.append(3)
		else:
			o0 = 8+o0
			x = x-x0
			o0 = 9/x
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))