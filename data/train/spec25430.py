import numpy as np 

def function(x):

	b3 = 4
	o0 = 3
	paths = []
	try:
		if b3 > 7:
			o0 = 1*6
			paths.append(1)
		else:
			x = x+o0
			o0 = x+o0
			paths.append(2)
		if o0 >= 4:
			o0 = x/o0
			x = x*1
			paths.append(3)
		else:
			o0 = b3*7
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