import numpy as np 

def function(x):

	r5 = x
	o2 = 0
	paths = []
	try:
		if x <= 0:
			r5 = 9-r5
			paths.append(1)
		else:
			o2 = 3*o2
			x = o2*4
			paths.append(2)
		if r5 <= 0:
			r5 = 4/o2
			x = 9*x
			paths.append(3)
		else:
			o2 = o2-r5
			r5 = 4-r5
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		r5 = o2**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))