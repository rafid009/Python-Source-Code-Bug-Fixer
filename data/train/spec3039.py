import numpy as np 

def function(x):

	a3 = 4
	o0 = 1
	paths = []
	try:
		if o0 >= 8:
			o0 = 7*o0
			paths.append(1)
		else:
			x = x+0
			o0 = o0+o0
			paths.append(2)
		if x >= 1:
			x = 2+9
			x = 8-8
			paths.append(3)
		else:
			x = 3+x
			o0 = o0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))