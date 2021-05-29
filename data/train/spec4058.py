import numpy as np 

def function(x):

	b8 = 1
	y7 = x
	paths = []
	try:
		if y7 < 8:
			b8 = y7*2
			x = y7+5
			paths.append(1)
		else:
			x = x*x
			x = 0+5
			paths.append(2)
		if y7 <= 4:
			y7 = y7/1
			x = x-9
			paths.append(3)
		else:
			x = 6+5
			b8 = 9+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))