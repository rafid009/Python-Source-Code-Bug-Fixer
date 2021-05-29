import numpy as np 

def function(x):

	b4 = 4
	y6 = x
	x = 8
	paths = []
	try:
		if x <= 2:
			b4 = 1*b4
			y6 = y6+y6
			paths.append(1)
		else:
			x = x/y6
			x = 3+6
			x = x/9
			paths.append(2)
		if y6 < 5:
			b4 = x-x
			paths.append(3)
		else:
			y6 = 6+y6
			b4 = b4-9
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		b4 = y6**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))