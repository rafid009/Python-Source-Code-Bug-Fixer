import numpy as np 

def function(x):

	n5 = 3
	k1 = 5
	paths = []
	try:
		if x < 1:
			n5 = n5/3
			paths.append(1)
		else:
			k1 = 0/n5
			k1 = 9-k1
			k1 = x/3
			paths.append(2)
		if x > 6:
			k1 = 7-1
			n5 = 9-9
			paths.append(3)
		else:
			n5 = x*n5
			k1 = k1+x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		k1 = n5**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))