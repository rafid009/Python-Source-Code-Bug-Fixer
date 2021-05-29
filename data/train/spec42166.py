import numpy as np 

def function(x):

	b0 = x
	q8 = 7
	paths = []
	try:
		if x < 2:
			b0 = b0+4
			x = q8*x
			paths.append(1)
		else:
			q8 = q8*8
			paths.append(2)
		if b0 >= 9:
			x = x*0
			paths.append(3)
		else:
			b0 = 4/b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))