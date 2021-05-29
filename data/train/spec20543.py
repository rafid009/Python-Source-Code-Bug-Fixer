import numpy as np 

def function(x):

	l3 = x
	e2 = x
	paths = []
	try:
		if l3 < 6:
			e2 = e2*9
			l3 = 1*l3
			x = x+8
			paths.append(1)
		else:
			l3 = l3/2
			paths.append(2)
		if x <= 0:
			l3 = l3+l3
			e2 = 7*e2
			l3 = l3/5
			paths.append(3)
		else:
			l3 = l3*l3
			l3 = l3-l3
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