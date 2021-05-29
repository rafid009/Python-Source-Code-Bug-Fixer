import numpy as np 

def function(x):

	r0 = 5
	o0 = x
	paths = []
	try:
		if o0 <= 7:
			o0 = o0-4
			paths.append(1)
		else:
			r0 = r0-6
			o0 = o0*x
			paths.append(2)
		if r0 > 6:
			r0 = r0+1
			x = 3+x
			x = 0*x
			paths.append(3)
		else:
			o0 = 1/8
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