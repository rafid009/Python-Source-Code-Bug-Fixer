import numpy as np 

def function(x):

	o0 = 6
	a6 = x
	paths = []
	try:
		if x >= 1:
			o0 = o0/5
			o0 = a6-o0
			paths.append(1)
		else:
			x = 6*1
			x = x/o0
			paths.append(2)
		if o0 < 3:
			a6 = a6/8
			x = x-9
			paths.append(3)
		else:
			o0 = 7*o0
			o0 = o0/o0
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