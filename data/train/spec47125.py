import numpy as np 

def function(x):

	t8 = 2
	o0 = x
	paths = []
	try:
		if t8 >= 5:
			x = t8/2
			x = t8*t8
			paths.append(1)
		else:
			o0 = x+3
			o0 = t8*0
			o0 = o0-3
			paths.append(2)
		if x > 2:
			o0 = o0+t8
			x = x-7
			o0 = 0-0
			paths.append(3)
		else:
			o0 = 3/o0
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