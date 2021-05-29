import numpy as np 

def function(x):

	k7 = 2
	r9 = x
	paths = []
	try:
		if x <= 5:
			k7 = k7-x
			k7 = 9*x
			k7 = k7*8
			paths.append(1)
		else:
			r9 = r9-9
			r9 = 6*8
			k7 = 1+6
			paths.append(2)
		if k7 > 0:
			k7 = 8*0
			paths.append(3)
		else:
			r9 = r9/9
			r9 = r9+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))