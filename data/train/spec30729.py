import numpy as np 

def function(x):

	o0 = x
	o7 = x
	paths = []
	try:
		if x < 1:
			o7 = 2-2
			paths.append(1)
		else:
			x = o0/x
			x = x/1
			paths.append(2)
		if x <= 8:
			x = 7+x
			o7 = x-x
			paths.append(3)
		else:
			x = x*x
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