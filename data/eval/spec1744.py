import numpy as np 

def function(x):

	a0 = x
	l6 = x
	paths = []
	try:
		if x <= 1:
			a0 = a0/a0
			x = 8-a0
			l6 = a0*l6
			paths.append(1)
		else:
			a0 = a0*x
			x = 3*x
			paths.append(2)
		if a0 <= 4:
			x = 9/3
			x = a0+a0
			x = a0*0
			paths.append(3)
		else:
			l6 = x-l6
			a0 = 1*4
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