import numpy as np 

def function(x):

	b8 = 2
	r5 = x
	paths = []
	try:
		if x > 8:
			x = 4-x
			r5 = 2+x
			r5 = b8-b8
			paths.append(1)
		else:
			r5 = r5+4
			b8 = 6*b8
			b8 = 3/b8
			paths.append(2)
		if b8 < 6:
			r5 = 4*4
			b8 = x*b8
			x = 0-x
			paths.append(3)
		else:
			b8 = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))