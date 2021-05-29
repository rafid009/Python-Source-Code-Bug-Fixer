import numpy as np 

def function(x):

	y2 = 6
	o0 = 0
	paths = []
	try:
		if o0 < 6:
			y2 = y2/7
			paths.append(1)
		else:
			o0 = y2*o0
			o0 = o0*3
			paths.append(2)
		if y2 > 6:
			x = 3/4
			paths.append(3)
		else:
			y2 = 7+y2
			x = x*1
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))