import numpy as np 

def function(x):

	k2 = x
	j8 = x
	paths = []
	try:
		if x >= 9:
			x = 9*2
			paths.append(1)
		else:
			x = 7*x
			x = x-k2
			x = x+5
			paths.append(2)
		if j8 < 2:
			k2 = 7-k2
			j8 = 6-6
			paths.append(3)
		else:
			j8 = j8*1
			k2 = 4+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))