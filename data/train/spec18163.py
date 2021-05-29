import numpy as np 

def function(x):

	a2 = x
	l6 = 1
	paths = []
	try:
		if x < 2:
			a2 = x-a2
			x = x*6
			a2 = 2-1
			paths.append(1)
		else:
			a2 = a2-x
			x = 3/x
			x = 2+2
			paths.append(2)
		if l6 <= 3:
			a2 = 3-l6
			l6 = l6-5
			a2 = 1/9
			paths.append(3)
		else:
			x = 3/x
			a2 = 6*a2
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		a2 = l6**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))