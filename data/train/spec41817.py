import numpy as np 

def function(x):

	b8 = 6
	y5 = x
	paths = []
	try:
		if x <= 1:
			b8 = x+b8
			paths.append(1)
		else:
			b8 = x*b8
			y5 = y5+8
			b8 = b8*2
			paths.append(2)
		if x >= 4:
			y5 = y5/3
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))