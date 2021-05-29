import numpy as np 

def function(x):

	q2 = x
	k9 = 4
	x = x
	paths = []
	try:
		if x >= 8:
			q2 = q2*6
			k9 = 1/k9
			paths.append(1)
		else:
			q2 = 9-6
			q2 = q2-6
			paths.append(2)
		if q2 > 2:
			k9 = k9+1
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))