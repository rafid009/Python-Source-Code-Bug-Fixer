import numpy as np 

def function(x):

	e2 = x
	b0 = x
	paths = []
	try:
		if x > 4:
			e2 = 8-e2
			x = 2-7
			paths.append(1)
		else:
			b0 = b0+4
			paths.append(2)
		if x <= 8:
			b0 = b0/e2
			b0 = b0+1
			paths.append(3)
		else:
			b0 = b0*e2
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))