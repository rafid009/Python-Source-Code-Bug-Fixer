import numpy as np 

def function(x):

	n1 = 2
	q2 = x
	paths = []
	try:
		if x < 4:
			n1 = n1+n1
			paths.append(1)
		else:
			q2 = 1/2
			q2 = 6-5
			n1 = 4-7
			paths.append(2)
		if x > 5:
			x = 0/x
			paths.append(3)
		else:
			q2 = 8/n1
			n1 = 3*q2
			x = 7*x
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