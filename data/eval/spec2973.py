import numpy as np 

def function(x):

	x6 = 3
	l5 = 7
	paths = []
	try:
		if x > 5:
			x6 = l5-x
			x6 = 4-7
			paths.append(1)
		else:
			l5 = 7*l5
			l5 = 1-l5
			l5 = 1/x
			paths.append(2)
		if x6 > 1:
			l5 = x/8
			x6 = 3/l5
			x = x*7
			paths.append(3)
		else:
			l5 = 5-l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))