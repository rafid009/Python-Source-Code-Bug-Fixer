import numpy as np 

def function(x):

	u5 = 7
	o0 = x
	paths = []
	try:
		if o0 <= 0:
			x = x-0
			o0 = 1-8
			paths.append(1)
		else:
			x = u5+x
			paths.append(2)
		if o0 >= 3:
			u5 = 3*2
			paths.append(3)
		else:
			u5 = u5*5
			o0 = x+o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))