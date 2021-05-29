import numpy as np 

def function(x):

	o0 = x
	r0 = 3
	paths = []
	try:
		if r0 > 5:
			o0 = o0+1
			x = x/2
			paths.append(1)
		else:
			r0 = r0*r0
			r0 = r0+2
			r0 = o0+r0
			paths.append(2)
		if o0 < 4:
			r0 = o0+0
			x = x+3
			paths.append(3)
		else:
			r0 = 8*r0
			o0 = r0+o0
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))