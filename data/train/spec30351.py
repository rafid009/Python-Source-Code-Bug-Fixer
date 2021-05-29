import numpy as np 

def function(x):

	m1 = x
	n7 = 2
	paths = []
	try:
		if m1 <= 5:
			n7 = 9-5
			n7 = n7-7
			paths.append(1)
		else:
			n7 = x-x
			paths.append(2)
		if n7 < 0:
			x = x/2
			paths.append(3)
		else:
			n7 = n7+8
			m1 = x/m1
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))