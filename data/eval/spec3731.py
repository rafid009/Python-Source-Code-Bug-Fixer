import numpy as np 

def function(x):

	q8 = x
	b0 = 2
	paths = []
	try:
		if b0 < 0:
			x = x/x
			b0 = b0-b0
			x = 4/x
			paths.append(1)
		else:
			q8 = q8/7
			b0 = b0/6
			paths.append(2)
		if b0 <= 2:
			x = 5/6
			x = 7/x
			b0 = b0/2
			paths.append(3)
		else:
			x = x*b0
			q8 = 7/3
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))