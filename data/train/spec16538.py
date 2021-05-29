import numpy as np 

def function(x):

	r2 = 9
	x2 = 7
	paths = []
	try:
		if r2 > 5:
			x2 = 0+4
			x2 = x+8
			r2 = 8*4
			paths.append(1)
		else:
			x2 = 2*2
			x = x-9
			paths.append(2)
		if x2 > 1:
			x = x2*0
			x2 = 4+5
			paths.append(3)
		else:
			x = x-0
			x2 = x2-3
			x2 = x/x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))