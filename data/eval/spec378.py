import numpy as np 

def function(x):

	x7 = 1
	b6 = x
	paths = []
	try:
		if b6 < 0:
			b6 = b6+2
			b6 = 5/b6
			paths.append(1)
		else:
			x7 = x-5
			x = x-4
			x = 7+x
			paths.append(2)
		if x7 <= 1:
			x7 = x7-6
			paths.append(3)
		else:
			x7 = x7+x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))