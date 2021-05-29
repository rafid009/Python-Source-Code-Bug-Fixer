import numpy as np 

def function(x):

	l6 = x
	b6 = x
	paths = []
	try:
		if b6 > 5:
			x = x/1
			paths.append(1)
		else:
			b6 = 0/8
			paths.append(2)
		if x >= 9:
			l6 = l6/6
			paths.append(3)
		else:
			l6 = l6*b6
			l6 = 6-b6
			b6 = 1-b6
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