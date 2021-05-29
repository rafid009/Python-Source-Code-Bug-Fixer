import numpy as np 

def function(x):

	x1 = 4
	b8 = x
	paths = []
	try:
		if x < 0:
			x1 = x1+x
			x1 = 8*x1
			b8 = 1+b8
			paths.append(1)
		else:
			b8 = b8+3
			x = 0+x
			paths.append(2)
		if x <= 3:
			x1 = x1+6
			x = 7*4
			paths.append(3)
		else:
			x = x+7
			b8 = b8*6
			x1 = x1-7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))