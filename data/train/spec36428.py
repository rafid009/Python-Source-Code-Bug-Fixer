import numpy as np 

def function(x):

	b2 = x
	w7 = x
	paths = []
	try:
		if x > 6:
			b2 = b2*x
			b2 = 1-b2
			paths.append(1)
		else:
			b2 = 5*4
			x = x+7
			paths.append(2)
		if x >= 6:
			x = 7*8
			x = 4-1
			x = 0*x
			paths.append(3)
		else:
			x = x*1
			w7 = b2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))