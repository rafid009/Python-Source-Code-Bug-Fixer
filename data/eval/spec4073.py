import numpy as np 

def function(x):

	k2 = 2
	i7 = 8
	paths = []
	try:
		if x <= 5:
			i7 = 3+6
			paths.append(1)
		else:
			x = i7/x
			i7 = 5*1
			paths.append(2)
		if x > 0:
			k2 = 5/1
			i7 = k2-i7
			paths.append(3)
		else:
			k2 = 0-k2
			x = x+i7
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))