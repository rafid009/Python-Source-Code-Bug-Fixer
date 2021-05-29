import numpy as np 

def function(x):

	r2 = x
	b7 = x
	paths = []
	try:
		if x >= 5:
			b7 = b7-4
			b7 = 4+b7
			r2 = r2*9
			paths.append(1)
		else:
			r2 = r2-2
			b7 = b7-7
			paths.append(2)
		if x < 0:
			b7 = 2*b7
			paths.append(3)
		else:
			r2 = b7+r2
			b7 = 6*2
			r2 = r2+x
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