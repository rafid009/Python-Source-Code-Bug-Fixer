import numpy as np 

def function(x):

	x4 = x
	b3 = x
	paths = []
	try:
		if x > 5:
			b3 = 3/x
			x4 = x4+x
			x4 = 0-8
			paths.append(1)
		else:
			b3 = x4+x
			x4 = x4/b3
			paths.append(2)
		if x4 >= 7:
			x = 4+5
			x4 = 2-8
			b3 = x4/8
			paths.append(3)
		else:
			x = x+x
			b3 = 0/2
			b3 = x-6
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x4 = b3**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))