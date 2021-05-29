import numpy as np 

def function(x):

	o0 = 8
	a1 = 5
	x = 2
	paths = []
	try:
		if a1 < 0:
			x = x-5
			o0 = o0-7
			paths.append(1)
		else:
			x = 0-5
			paths.append(2)
		if x < 0:
			a1 = 1-a1
			o0 = x/o0
			x = x-x
			paths.append(3)
		else:
			o0 = 5/4
			x = x+3
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))