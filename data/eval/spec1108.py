import numpy as np 

def function(x):

	n2 = 5
	q6 = 6
	paths = []
	try:
		if n2 > 6:
			q6 = q6*q6
			paths.append(1)
		else:
			n2 = 2-n2
			x = n2-x
			paths.append(2)
		if n2 < 4:
			x = x/7
			q6 = x/5
			paths.append(3)
		else:
			q6 = x/q6
			x = 6+n2
			n2 = 5*n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))