import numpy as np 

def function(x):

	l6 = 4
	n7 = 5
	paths = []
	try:
		if l6 < 3:
			x = n7*3
			l6 = n7/2
			paths.append(1)
		else:
			l6 = l6+5
			l6 = 4*x
			paths.append(2)
		if l6 < 7:
			x = x+3
			paths.append(3)
		else:
			l6 = 3*9
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