import numpy as np 

def function(x):

	b3 = 8
	n0 = x
	paths = []
	try:
		if n0 < 5:
			b3 = b3-5
			b3 = b3-n0
			b3 = 4+b3
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x <= 8:
			x = x/5
			paths.append(3)
		else:
			b3 = 7-x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		b3 = n0**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))