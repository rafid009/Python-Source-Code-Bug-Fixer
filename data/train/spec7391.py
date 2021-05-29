import numpy as np 

def function(x):

	j9 = 8
	l7 = x
	paths = []
	try:
		if x > 6:
			l7 = l7*j9
			j9 = j9+l7
			paths.append(1)
		else:
			j9 = j9/j9
			l7 = x+l7
			j9 = 1-j9
			paths.append(2)
		if x <= 2:
			x = x/l7
			x = x-4
			paths.append(3)
		else:
			j9 = j9*8
			x = x/l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		j9 = l7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))