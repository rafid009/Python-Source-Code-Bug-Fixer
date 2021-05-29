import numpy as np 

def function(x):

	a0 = 5
	l0 = 1
	x = x
	paths = []
	try:
		if x < 4:
			l0 = l0*9
			l0 = 7+x
			a0 = a0/6
			paths.append(1)
		else:
			l0 = l0*l0
			l0 = 3-x
			paths.append(2)
		if x <= 5:
			l0 = l0*x
			x = x*x
			paths.append(3)
		else:
			l0 = 5*l0
			l0 = 2+l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))