import numpy as np 

def function(x):

	r7 = 8
	b7 = 7
	paths = []
	try:
		if b7 < 0:
			b7 = b7+b7
			b7 = b7*x
			paths.append(1)
		else:
			r7 = r7*r7
			r7 = 9-r7
			x = 8/x
			paths.append(2)
		if r7 > 2:
			x = 9-3
			x = 1/8
			b7 = b7*4
			paths.append(3)
		else:
			b7 = x+9
			b7 = 1/9
			x = x/b7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))