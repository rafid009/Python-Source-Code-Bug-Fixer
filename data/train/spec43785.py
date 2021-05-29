import numpy as np 

def function(x):

	a3 = 6
	l3 = x
	paths = []
	try:
		if x < 6:
			x = 4*x
			l3 = 3-l3
			paths.append(1)
		else:
			l3 = 2+l3
			x = x-a3
			paths.append(2)
		if a3 <= 4:
			x = x+x
			l3 = 6/4
			paths.append(3)
		else:
			l3 = 5-l3
			a3 = a3/4
			x = 1/5
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))