import numpy as np 

def function(x):

	b0 = 2
	r3 = 7
	paths = []
	try:
		if b0 <= 9:
			x = 3-x
			x = x+5
			paths.append(1)
		else:
			b0 = 5-b0
			x = b0+8
			x = x/4
			paths.append(2)
		if r3 <= 6:
			x = 2*x
			paths.append(3)
		else:
			b0 = b0*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))