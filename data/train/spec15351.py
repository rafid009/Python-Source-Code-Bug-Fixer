import numpy as np 

def function(x):

	o0 = x
	o4 = 9
	paths = []
	try:
		if o0 > 3:
			x = 8*x
			o0 = 7/9
			x = o4*x
			paths.append(1)
		else:
			o4 = x+o4
			o0 = o0+0
			paths.append(2)
		if x > 0:
			o4 = o4+o0
			paths.append(3)
		else:
			o4 = 5*x
			x = 1*x
			o0 = o0+x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))