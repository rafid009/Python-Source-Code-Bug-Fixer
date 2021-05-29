import numpy as np 

def function(x):

	k3 = x
	q3 = x
	paths = []
	try:
		if x >= 1:
			k3 = 5*9
			x = x*4
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if q3 > 6:
			x = 6+3
			paths.append(3)
		else:
			q3 = 0-k3
			k3 = 2/8
			x = 3+4
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))