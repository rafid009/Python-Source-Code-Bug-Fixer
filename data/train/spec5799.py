import numpy as np 

def function(x):

	k9 = 3
	y7 = x
	x = x
	paths = []
	try:
		if k9 <= 0:
			k9 = x/k9
			paths.append(1)
		else:
			y7 = y7-k9
			paths.append(2)
		if x <= 0:
			x = y7-3
			paths.append(3)
		else:
			k9 = 7+k9
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))