import numpy as np 

def function(x):

	l5 = x
	j2 = 8
	paths = []
	try:
		if x <= 6:
			l5 = l5+j2
			paths.append(1)
		else:
			j2 = 2/j2
			l5 = j2/7
			x = 5+6
			paths.append(2)
		if x <= 1:
			x = 5+8
			j2 = l5+j2
			paths.append(3)
		else:
			x = 1*4
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