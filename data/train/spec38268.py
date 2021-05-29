import numpy as np 

def function(x):

	o2 = 5
	r9 = x
	paths = []
	try:
		if x < 7:
			o2 = o2/r9
			paths.append(1)
		else:
			o2 = 3-7
			o2 = o2+2
			paths.append(2)
		if x <= 1:
			o2 = x+1
			r9 = r9+6
			paths.append(3)
		else:
			x = x*4
			o2 = 5-o2
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