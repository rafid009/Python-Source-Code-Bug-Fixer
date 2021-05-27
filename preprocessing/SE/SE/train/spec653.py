import numpy as np 

def function(x):

	o4 = x
	r3 = 7
	paths = []
	try:
		if o4 < 9:
			r3 = x+9
			paths.append(1)
		else:
			o4 = 2*6
			paths.append(2)
		if x <= 4:
			x = r3*5
			o4 = x-9
			paths.append(3)
		else:
			r3 = r3*o4
			x = 5+x
			x = 2/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))