import numpy as np 

def function(x):

	a3 = 9
	l1 = 3
	paths = []
	try:
		if a3 < 5:
			l1 = 5+9
			paths.append(1)
		else:
			l1 = l1+5
			paths.append(2)
		if l1 >= 5:
			a3 = x*a3
			paths.append(3)
		else:
			l1 = l1*x
			l1 = 4*l1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))