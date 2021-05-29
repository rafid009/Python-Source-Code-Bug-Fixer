import numpy as np 

def function(x):

	l7 = 5
	k9 = 5
	paths = []
	try:
		if x >= 9:
			k9 = 1+k9
			paths.append(1)
		else:
			l7 = 1/8
			paths.append(2)
		if k9 < 6:
			l7 = l7-5
			l7 = 5+l7
			paths.append(3)
		else:
			k9 = 9+k9
			l7 = 2-l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))