import numpy as np 

def function(x):

	l3 = x
	a3 = x
	paths = []
	try:
		if x <= 9:
			a3 = 8*a3
			paths.append(1)
		else:
			l3 = 2+7
			a3 = 1*a3
			paths.append(2)
		if a3 >= 3:
			x = x+x
			l3 = 3-a3
			a3 = a3*3
			paths.append(3)
		else:
			l3 = 2/l3
			a3 = l3-x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		a3 = l3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))