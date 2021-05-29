import numpy as np 

def function(x):

	i6 = 7
	o0 = 3
	paths = []
	try:
		if o0 > 8:
			o0 = 5-8
			x = o0*x
			o0 = x-4
			paths.append(1)
		else:
			o0 = 6/4
			paths.append(2)
		if x < 2:
			o0 = 6+o0
			o0 = i6/5
			paths.append(3)
		else:
			o0 = 2/5
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))