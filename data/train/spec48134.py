import numpy as np 

def function(x):

	q9 = 9
	p7 = x
	paths = []
	try:
		if q9 < 9:
			x = p7*x
			p7 = 7-p7
			p7 = 5/p7
			paths.append(1)
		else:
			x = 2/7
			paths.append(2)
		if x <= 2:
			q9 = p7/7
			x = p7-x
			paths.append(3)
		else:
			p7 = p7+2
			x = x/2
			x = x-6
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))