import numpy as np 

def function(x):

	k4 = 1
	o0 = 1
	paths = []
	try:
		if x > 1:
			k4 = 7+0
			paths.append(1)
		else:
			k4 = 5-6
			x = x-3
			paths.append(2)
		if o0 < 9:
			o0 = 7-o0
			x = x/3
			paths.append(3)
		else:
			k4 = k4*0
			k4 = 1*o0
			k4 = k4-k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))