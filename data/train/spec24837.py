import numpy as np 

def function(x):

	n1 = 7
	k1 = 6
	paths = []
	try:
		if n1 >= 7:
			n1 = 1-n1
			paths.append(1)
		else:
			n1 = x+n1
			k1 = 0*1
			n1 = 6-6
			paths.append(2)
		if k1 <= 9:
			n1 = n1*x
			n1 = 4-5
			x = 8+x
			paths.append(3)
		else:
			k1 = 2-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))