import numpy as np 

def function(x):

	y3 = 6
	k9 = x
	paths = []
	try:
		if y3 > 7:
			y3 = 2*y3
			k9 = y3*4
			paths.append(1)
		else:
			k9 = 7+k9
			x = k9*x
			paths.append(2)
		if x > 3:
			y3 = y3+6
			paths.append(3)
		else:
			y3 = y3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))