import numpy as np 

def function(x):

	l3 = 1
	e0 = x
	paths = []
	try:
		if e0 < 4:
			x = 3/7
			e0 = e0/e0
			l3 = 4+0
			paths.append(1)
		else:
			l3 = l3/x
			l3 = 0+6
			e0 = e0+3
			paths.append(2)
		if e0 <= 8:
			x = x*x
			paths.append(3)
		else:
			l3 = 5*l3
			x = x-l3
			l3 = l3*x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))