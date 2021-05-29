import numpy as np 

def function(x):

	o0 = x
	r0 = 1
	paths = []
	try:
		if o0 < 3:
			r0 = 6*r0
			paths.append(1)
		else:
			o0 = o0-6
			paths.append(2)
		if o0 <= 4:
			o0 = o0-7
			o0 = r0*x
			o0 = o0/x
			paths.append(3)
		else:
			o0 = 1*r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))