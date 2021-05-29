import numpy as np 

def function(x):

	k1 = x
	l6 = 3
	paths = []
	try:
		if l6 >= 2:
			l6 = 3+k1
			l6 = k1-l6
			l6 = k1*l6
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if l6 < 4:
			x = 4+l6
			k1 = k1+3
			k1 = k1/x
			paths.append(3)
		else:
			l6 = x+6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))