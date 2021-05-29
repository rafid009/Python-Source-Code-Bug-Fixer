import numpy as np 

def function(x):

	j9 = x
	k1 = 7
	paths = []
	try:
		if x > 3:
			k1 = 8/k1
			k1 = 6+k1
			paths.append(1)
		else:
			j9 = j9-9
			j9 = j9-5
			k1 = k1*x
			paths.append(2)
		if j9 < 1:
			j9 = 2/j9
			x = x/6
			paths.append(3)
		else:
			k1 = k1-9
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