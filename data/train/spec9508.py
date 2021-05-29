import numpy as np 

def function(x):

	u9 = x
	o0 = x
	paths = []
	try:
		if o0 < 9:
			x = u9*1
			paths.append(1)
		else:
			o0 = 1-6
			paths.append(2)
		if o0 < 3:
			u9 = u9/u9
			u9 = o0*u9
			o0 = x+1
			paths.append(3)
		else:
			o0 = o0-2
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