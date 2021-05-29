import numpy as np 

def function(x):

	o8 = x
	k1 = x
	paths = []
	try:
		if k1 <= 6:
			k1 = k1-1
			o8 = 4+o8
			o8 = 8+x
			paths.append(1)
		else:
			o8 = 8*o8
			x = 8/7
			paths.append(2)
		if x < 1:
			x = x-k1
			x = 9*1
			k1 = k1/2
			paths.append(3)
		else:
			o8 = 1*o8
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))