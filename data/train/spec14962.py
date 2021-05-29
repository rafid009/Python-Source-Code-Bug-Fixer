import numpy as np 

def function(x):

	k3 = 7
	q6 = x
	paths = []
	try:
		if q6 > 9:
			x = x/9
			x = x/2
			paths.append(1)
		else:
			q6 = k3/q6
			paths.append(2)
		if q6 > 5:
			q6 = q6/5
			k3 = 9+k3
			paths.append(3)
		else:
			x = 2-x
			k3 = k3*q6
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))