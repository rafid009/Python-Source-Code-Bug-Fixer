import numpy as np 

def function(x):

	k6 = x
	q5 = x
	paths = []
	try:
		if q5 > 7:
			k6 = 0-x
			paths.append(1)
		else:
			q5 = 3-q5
			k6 = k6/q5
			paths.append(2)
		if k6 >= 6:
			q5 = 2*k6
			k6 = k6/2
			paths.append(3)
		else:
			k6 = k6*6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))