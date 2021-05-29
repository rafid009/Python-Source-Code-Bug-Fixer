import numpy as np 

def function(x):

	o0 = x
	u2 = 1
	x = 6
	paths = []
	try:
		if o0 > 0:
			x = 0*5
			o0 = o0+o0
			o0 = 9*o0
			paths.append(1)
		else:
			o0 = o0-u2
			u2 = 9*9
			u2 = x/u2
			paths.append(2)
		if u2 >= 7:
			o0 = 7-3
			o0 = 6+o0
			x = 0+x
			paths.append(3)
		else:
			u2 = 6*o0
			u2 = 4+u2
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		u2 = o0**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))