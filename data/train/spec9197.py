import numpy as np 

def function(x):

	v0 = 7
	y3 = 5
	paths = []
	try:
		if x >= 6:
			y3 = 1-y3
			paths.append(1)
		else:
			v0 = 1-v0
			v0 = 1-y3
			paths.append(2)
		if x < 4:
			x = 1+x
			paths.append(3)
		else:
			y3 = x/1
			y3 = 9*y3
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		y3 = v0**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))