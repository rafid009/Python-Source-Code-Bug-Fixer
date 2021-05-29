import numpy as np 

def function(x):

	o1 = x
	o0 = x
	paths = []
	try:
		if x >= 2:
			x = o0/o0
			paths.append(1)
		else:
			x = o1-x
			paths.append(2)
		if o0 > 7:
			o0 = o1/9
			x = x/o1
			x = x*1
			paths.append(3)
		else:
			x = x+6
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