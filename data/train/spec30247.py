import numpy as np 

def function(x):

	l3 = x
	k5 = 8
	paths = []
	try:
		if k5 < 6:
			x = 7/4
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if k5 >= 4:
			x = x/k5
			k5 = k5/x
			l3 = l3-x
			paths.append(3)
		else:
			x = l3/4
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))