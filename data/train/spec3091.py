import numpy as np 

def function(x):

	o0 = x
	a7 = x
	paths = []
	try:
		if a7 > 6:
			x = x/x
			paths.append(1)
		else:
			o0 = 2-a7
			o0 = o0+a7
			a7 = a7-8
			paths.append(2)
		if a7 > 6:
			a7 = x/a7
			a7 = 9/a7
			x = x/8
			paths.append(3)
		else:
			x = x*a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		o0 = a7**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))