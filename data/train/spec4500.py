import numpy as np 

def function(x):

	z7 = x
	o0 = 4
	paths = []
	try:
		if o0 >= 8:
			o0 = o0+o0
			paths.append(1)
		else:
			o0 = o0+x
			o0 = o0+5
			o0 = 3*2
			paths.append(2)
		if z7 < 4:
			z7 = z7+9
			o0 = 2*o0
			x = 8-x
			paths.append(3)
		else:
			x = 4*3
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		o0 = z7**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))