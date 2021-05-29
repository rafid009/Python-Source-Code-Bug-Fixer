import numpy as np 

def function(x):

	x8 = 8
	b9 = 2
	paths = []
	try:
		if b9 > 2:
			b9 = 6/b9
			b9 = b9+b9
			x = 6+x8
			paths.append(1)
		else:
			x8 = 3-x8
			b9 = b9-7
			x8 = x8/x
			paths.append(2)
		if x <= 5:
			x = x/8
			x8 = x8-x8
			paths.append(3)
		else:
			b9 = x-b9
			x = 3-6
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x8 = b9**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))