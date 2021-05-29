import numpy as np 

def function(x):

	o0 = x
	v2 = 7
	paths = []
	try:
		if x < 4:
			x = 2-x
			paths.append(1)
		else:
			x = v2+6
			o0 = o0/7
			v2 = v2/8
			paths.append(2)
		if x > 6:
			o0 = 1*o0
			paths.append(3)
		else:
			o0 = 3+o0
			v2 = o0+3
			x = x-8
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