import numpy as np 

def function(x):

	r0 = 3
	o6 = 3
	paths = []
	try:
		if x > 5:
			x = x/4
			r0 = r0*3
			x = x/1
			paths.append(1)
		else:
			r0 = 9/r0
			x = x-5
			r0 = r0-r0
			paths.append(2)
		if r0 > 6:
			r0 = r0-8
			paths.append(3)
		else:
			x = r0/x
			o6 = 2-4
			r0 = 4*2
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		r0 = o6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))