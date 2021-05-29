import numpy as np 

def function(x):

	r0 = 6
	o8 = 7
	paths = []
	try:
		if r0 < 5:
			r0 = o8*o8
			x = x-0
			x = x/r0
			paths.append(1)
		else:
			x = x+2
			x = x*o8
			x = x+6
			paths.append(2)
		if o8 <= 6:
			x = o8*r0
			paths.append(3)
		else:
			o8 = r0/x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		r0 = o8**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))