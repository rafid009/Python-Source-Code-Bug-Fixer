import numpy as np 

def function(x):

	l7 = 2
	j8 = 3
	paths = []
	try:
		if j8 <= 2:
			j8 = x*6
			l7 = 7+5
			j8 = 8/3
			paths.append(1)
		else:
			l7 = 2+5
			paths.append(2)
		if x >= 7:
			x = x+8
			l7 = l7-x
			paths.append(3)
		else:
			l7 = j8+l7
			j8 = j8-0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))