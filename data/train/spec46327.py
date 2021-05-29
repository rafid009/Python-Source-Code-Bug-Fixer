import numpy as np 

def function(x):

	y8 = x
	r6 = x
	paths = []
	try:
		if y8 > 1:
			x = x/4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if r6 <= 7:
			x = 3+x
			y8 = y8-1
			paths.append(3)
		else:
			x = x*4
			x = 8-x
			x = x/r6
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