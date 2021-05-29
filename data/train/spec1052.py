import numpy as np 

def function(x):

	o7 = 6
	o0 = 1
	paths = []
	try:
		if o7 < 3:
			x = o0+1
			paths.append(1)
		else:
			o0 = 1-1
			paths.append(2)
		if o7 < 0:
			o7 = x/1
			o0 = o0-8
			o0 = o7*o0
			paths.append(3)
		else:
			o7 = 1/o7
			o0 = x*8
			x = x-o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))