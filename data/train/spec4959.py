import numpy as np 

def function(x):

	o0 = 4
	i1 = 4
	x = x
	paths = []
	try:
		if o0 < 7:
			i1 = 1+i1
			paths.append(1)
		else:
			o0 = 6*o0
			paths.append(2)
		if x > 8:
			o0 = 2/8
			o0 = o0-i1
			paths.append(3)
		else:
			o0 = o0*o0
			x = 8-x
			x = x+o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		i1 = o0**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))