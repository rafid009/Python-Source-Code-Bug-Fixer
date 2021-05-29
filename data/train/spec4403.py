import numpy as np 

def function(x):

	o6 = 8
	r7 = 8
	paths = []
	try:
		if x <= 8:
			o6 = x+o6
			r7 = o6+1
			o6 = x-o6
			paths.append(1)
		else:
			o6 = 9-o6
			r7 = r7-r7
			paths.append(2)
		if o6 < 0:
			o6 = 0/x
			o6 = o6/5
			x = x+o6
			paths.append(3)
		else:
			o6 = 1-o6
			r7 = 2-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))