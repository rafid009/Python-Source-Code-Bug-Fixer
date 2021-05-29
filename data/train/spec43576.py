import numpy as np 

def function(x):

	q0 = x
	l3 = x
	paths = []
	try:
		if l3 >= 8:
			q0 = 4-9
			paths.append(1)
		else:
			x = q0+x
			paths.append(2)
		if q0 >= 1:
			l3 = 5*l3
			paths.append(3)
		else:
			x = 1*x
			q0 = x+q0
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