import numpy as np 

def function(x):

	y7 = x
	z9 = 1
	paths = []
	try:
		if z9 <= 2:
			y7 = 8+x
			y7 = 0+z9
			paths.append(1)
		else:
			y7 = y7+2
			x = x/3
			paths.append(2)
		if y7 < 6:
			x = x*2
			y7 = y7*4
			z9 = x/z9
			paths.append(3)
		else:
			y7 = 8+y7
			x = 7/x
			y7 = y7+1
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