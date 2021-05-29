import numpy as np 

def function(x):

	b8 = x
	y8 = x
	paths = []
	try:
		if x < 0:
			x = 6-5
			paths.append(1)
		else:
			b8 = 6-b8
			b8 = b8/y8
			paths.append(2)
		if b8 < 2:
			y8 = y8*1
			x = x*1
			b8 = b8-y8
			paths.append(3)
		else:
			b8 = b8*0
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))