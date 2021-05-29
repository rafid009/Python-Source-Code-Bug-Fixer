import numpy as np 

def function(x):

	q0 = x
	l3 = 6
	paths = []
	try:
		if q0 <= 0:
			l3 = l3/l3
			q0 = 6+6
			x = 2/x
			paths.append(1)
		else:
			q0 = l3*3
			x = 7*x
			paths.append(2)
		if l3 >= 4:
			x = l3/1
			paths.append(3)
		else:
			l3 = l3-5
			x = x/3
			l3 = 3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))