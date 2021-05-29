import numpy as np 

def function(x):

	b2 = x
	x5 = 7
	paths = []
	try:
		if b2 > 8:
			x = x*b2
			x5 = x5+x5
			x5 = b2-x5
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if x > 8:
			x = x*b2
			paths.append(3)
		else:
			x5 = x5-b2
			x = x*4
			x = 0+0
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))