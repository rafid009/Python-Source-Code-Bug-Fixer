import numpy as np 

def function(x):

	r8 = x
	b2 = x
	paths = []
	try:
		if b2 <= 8:
			b2 = b2-2
			r8 = 8*6
			r8 = r8-2
			paths.append(1)
		else:
			x = x+x
			r8 = 2/r8
			paths.append(2)
		if x >= 9:
			b2 = 5-2
			b2 = b2-r8
			paths.append(3)
		else:
			x = x/r8
			r8 = r8+r8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))