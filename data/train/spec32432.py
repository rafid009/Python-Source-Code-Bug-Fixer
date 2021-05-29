import numpy as np 

def function(x):

	x6 = x
	n1 = x
	x = 0
	paths = []
	try:
		if x > 2:
			x = x*8
			x = n1/3
			paths.append(1)
		else:
			x = x-8
			x6 = x6*x6
			paths.append(2)
		if n1 <= 2:
			x6 = 1*n1
			paths.append(3)
		else:
			n1 = 7*6
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))