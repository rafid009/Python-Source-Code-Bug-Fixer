import numpy as np 

def function(x):

	f0 = 0
	o0 = x
	paths = []
	try:
		if x > 1:
			x = x/5
			f0 = f0/8
			paths.append(1)
		else:
			o0 = o0*f0
			o0 = o0-5
			x = 2+x
			paths.append(2)
		if x > 2:
			o0 = o0/x
			paths.append(3)
		else:
			x = 7/x
			o0 = 7-o0
			f0 = f0+4
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