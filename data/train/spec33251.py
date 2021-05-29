import numpy as np 

def function(x):

	e5 = 2
	o0 = 7
	paths = []
	try:
		if e5 > 3:
			e5 = x/3
			x = 7/e5
			paths.append(1)
		else:
			x = x-o0
			paths.append(2)
		if e5 > 6:
			e5 = 9+e5
			o0 = x+x
			x = x/7
			paths.append(3)
		else:
			e5 = 1+1
			x = x/7
			e5 = 5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))