import numpy as np 

def function(x):

	l6 = x
	x3 = 9
	paths = []
	try:
		if x3 > 7:
			x3 = x-l6
			l6 = l6+2
			x3 = x3/5
			paths.append(1)
		else:
			x3 = x3*x
			x = x-2
			paths.append(2)
		if x3 > 0:
			l6 = l6*l6
			x3 = x3+7
			x = x3/7
			paths.append(3)
		else:
			x3 = x3/9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x3 = l6**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))