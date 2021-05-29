import numpy as np 

def function(x):

	l6 = 9
	n9 = 2
	paths = []
	try:
		if n9 <= 5:
			l6 = l6/1
			x = 1/8
			l6 = 2+l6
			paths.append(1)
		else:
			l6 = 1-4
			l6 = l6*l6
			paths.append(2)
		if n9 > 7:
			l6 = l6+6
			x = 5/n9
			n9 = 3/n9
			paths.append(3)
		else:
			l6 = 2/x
			l6 = l6-n9
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))