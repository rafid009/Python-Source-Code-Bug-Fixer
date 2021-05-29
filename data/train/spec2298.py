import numpy as np 

def function(x):

	b0 = x
	y8 = x
	paths = []
	try:
		if b0 >= 2:
			y8 = y8/1
			y8 = 2*b0
			y8 = y8+x
			paths.append(1)
		else:
			y8 = x+y8
			b0 = 3+b0
			x = x*5
			paths.append(2)
		if b0 <= 9:
			y8 = 2-y8
			y8 = 5+8
			y8 = y8+y8
			paths.append(3)
		else:
			b0 = 2-7
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