import numpy as np 

def function(x):

	x7 = x
	r9 = 7
	paths = []
	try:
		if x >= 0:
			r9 = 8*0
			x = r9+x7
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x7 < 1:
			x = x*1
			r9 = r9+8
			x = 5+x
			paths.append(3)
		else:
			x = 1*7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))