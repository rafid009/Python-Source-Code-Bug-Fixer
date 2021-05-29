import numpy as np 

def function(x):

	k1 = 2
	n1 = x
	paths = []
	try:
		if x < 1:
			n1 = n1+n1
			x = 0/k1
			k1 = 7/1
			paths.append(1)
		else:
			k1 = k1*x
			paths.append(2)
		if k1 <= 5:
			n1 = n1/3
			paths.append(3)
		else:
			n1 = 8/n1
			k1 = n1-0
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