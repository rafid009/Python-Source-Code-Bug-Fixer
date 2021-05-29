import numpy as np 

def function(x):

	k3 = x
	q7 = 3
	paths = []
	try:
		if x >= 8:
			k3 = k3+7
			k3 = x+9
			paths.append(1)
		else:
			q7 = 9-4
			paths.append(2)
		if x > 0:
			k3 = k3/q7
			x = x+k3
			k3 = 0+x
			paths.append(3)
		else:
			q7 = 9*q7
			q7 = q7/4
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		q7 = k3**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))