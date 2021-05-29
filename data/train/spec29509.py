import numpy as np 

def function(x):

	k3 = 6
	l6 = x
	paths = []
	try:
		if l6 < 3:
			k3 = k3-2
			paths.append(1)
		else:
			x = 0/7
			paths.append(2)
		if k3 <= 0:
			k3 = l6+l6
			k3 = x-1
			paths.append(3)
		else:
			l6 = l6+0
			l6 = 0-9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))