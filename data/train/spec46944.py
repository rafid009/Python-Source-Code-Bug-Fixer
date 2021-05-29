import numpy as np 

def function(x):

	q0 = x
	a6 = 6
	paths = []
	try:
		if x >= 0:
			x = x+a6
			a6 = 0/3
			x = x*a6
			paths.append(1)
		else:
			x = 0+x
			x = q0+1
			x = x*3
			paths.append(2)
		if a6 <= 7:
			x = 9+x
			q0 = 3*8
			a6 = x-5
			paths.append(3)
		else:
			x = x*x
			a6 = a6-q0
			a6 = 4+q0
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