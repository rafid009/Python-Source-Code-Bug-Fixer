import numpy as np 

def function(x):

	o0 = x
	r2 = x
	paths = []
	try:
		if x <= 3:
			o0 = 7-o0
			r2 = 6*0
			paths.append(1)
		else:
			x = x+2
			x = 6-o0
			r2 = x*r2
			paths.append(2)
		if x > 3:
			o0 = x-o0
			x = 5/o0
			x = 9-x
			paths.append(3)
		else:
			o0 = 4+1
			x = 1-4
			r2 = 2+o0
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