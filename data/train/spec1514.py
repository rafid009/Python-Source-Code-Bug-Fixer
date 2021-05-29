import numpy as np 

def function(x):

	k5 = x
	j6 = x
	paths = []
	try:
		if x > 4:
			k5 = k5/7
			paths.append(1)
		else:
			j6 = j6*9
			paths.append(2)
		if k5 >= 2:
			j6 = j6*3
			k5 = k5-5
			x = x-j6
			paths.append(3)
		else:
			k5 = x-k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))