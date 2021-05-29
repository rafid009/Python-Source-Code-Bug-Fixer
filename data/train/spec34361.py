import numpy as np 

def function(x):

	r9 = x
	o7 = 3
	paths = []
	try:
		if r9 <= 3:
			o7 = x*o7
			paths.append(1)
		else:
			r9 = 3-r9
			paths.append(2)
		if x < 4:
			x = 6/x
			x = x+x
			paths.append(3)
		else:
			o7 = 1/o7
			x = 3+2
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))