import numpy as np 

def function(x):

	r9 = x
	b2 = x
	paths = []
	try:
		if b2 < 6:
			r9 = 2/2
			paths.append(1)
		else:
			x = x+x
			x = x*b2
			x = x*5
			paths.append(2)
		if b2 >= 5:
			x = x*b2
			x = r9-x
			paths.append(3)
		else:
			r9 = r9-0
			r9 = x/r9
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))