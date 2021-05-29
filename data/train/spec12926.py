import numpy as np 

def function(x):

	k1 = 7
	l6 = x
	x = 0
	paths = []
	try:
		if k1 >= 5:
			k1 = k1+l6
			x = l6*4
			paths.append(1)
		else:
			x = l6*x
			paths.append(2)
		if l6 < 0:
			l6 = x*7
			l6 = l6+8
			k1 = l6*9
			paths.append(3)
		else:
			l6 = l6*4
			x = x/4
			k1 = k1-1
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