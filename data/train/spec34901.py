import numpy as np 

def function(x):

	a9 = 9
	n1 = x
	paths = []
	try:
		if n1 > 5:
			n1 = 7*n1
			a9 = 0+a9
			n1 = n1/1
			paths.append(1)
		else:
			n1 = a9+4
			a9 = a9-n1
			paths.append(2)
		if x < 0:
			a9 = 9-5
			n1 = n1+9
			paths.append(3)
		else:
			x = 6*x
			n1 = n1*n1
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		n1 = a9**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))