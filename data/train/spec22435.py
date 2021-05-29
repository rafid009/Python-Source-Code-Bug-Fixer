import numpy as np 

def function(x):

	b3 = 2
	y7 = x
	x = 9
	paths = []
	try:
		if x <= 7:
			x = b3/x
			paths.append(1)
		else:
			x = x/9
			y7 = b3/y7
			paths.append(2)
		if b3 >= 7:
			b3 = b3-7
			b3 = x/7
			y7 = 2/9
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		b3 = y7**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))