import numpy as np 

def function(x):

	b0 = x
	r6 = 2
	paths = []
	try:
		if r6 < 8:
			b0 = b0/7
			paths.append(1)
		else:
			b0 = 1*7
			paths.append(2)
		if r6 <= 0:
			b0 = b0*3
			r6 = r6*7
			b0 = b0+8
			paths.append(3)
		else:
			r6 = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))