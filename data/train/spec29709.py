import numpy as np 

def function(x):

	n4 = 9
	m1 = x
	paths = []
	try:
		if n4 < 6:
			n4 = 9/x
			n4 = x+2
			x = n4/n4
			paths.append(1)
		else:
			n4 = n4-n4
			x = x-5
			paths.append(2)
		if n4 < 1:
			n4 = n4*x
			paths.append(3)
		else:
			n4 = 5*n4
			m1 = 5/m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))