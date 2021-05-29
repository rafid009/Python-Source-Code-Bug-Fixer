import numpy as np 

def function(x):

	y8 = 1
	q8 = x
	x = 4
	paths = []
	try:
		if q8 > 1:
			q8 = 7+x
			y8 = 6-y8
			x = 2+x
			paths.append(1)
		else:
			y8 = 8*y8
			y8 = 3+5
			y8 = 1+6
			paths.append(2)
		if y8 < 0:
			x = x-8
			q8 = q8/1
			x = x-4
			paths.append(3)
		else:
			q8 = x-q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))