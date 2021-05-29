import numpy as np 

def function(x):

	b2 = 8
	e7 = 5
	paths = []
	try:
		if b2 < 8:
			e7 = 4/e7
			x = e7-1
			e7 = e7/8
			paths.append(1)
		else:
			x = 3-x
			b2 = b2*8
			paths.append(2)
		if b2 >= 5:
			e7 = e7/5
			x = 8+x
			paths.append(3)
		else:
			e7 = x*e7
			x = 5*5
			b2 = b2-4
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