import numpy as np 

def function(x):

	l0 = x
	k6 = x
	paths = []
	try:
		if k6 < 7:
			l0 = 8+k6
			l0 = 8+l0
			paths.append(1)
		else:
			l0 = l0-8
			paths.append(2)
		if k6 > 5:
			x = x-8
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		l0 = k6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))