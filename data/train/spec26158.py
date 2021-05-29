import numpy as np 

def function(x):

	y5 = x
	q2 = x
	paths = []
	try:
		if x <= 2:
			q2 = 4*q2
			y5 = y5+5
			y5 = q2+y5
			paths.append(1)
		else:
			q2 = q2-7
			x = 9+q2
			x = 8/x
			paths.append(2)
		if y5 <= 4:
			q2 = x/9
			paths.append(3)
		else:
			q2 = y5*7
			q2 = q2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))