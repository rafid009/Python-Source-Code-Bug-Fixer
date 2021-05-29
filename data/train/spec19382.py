import numpy as np 

def function(x):

	x5 = 8
	i6 = 6
	paths = []
	try:
		if x < 6:
			x5 = x5-2
			paths.append(1)
		else:
			x5 = i6-8
			x5 = x5*i6
			paths.append(2)
		if i6 > 1:
			x5 = 8*x5
			x = x*8
			paths.append(3)
		else:
			x = 8+x5
			x5 = x5+7
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))