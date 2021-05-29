import numpy as np 

def function(x):

	q0 = x
	a2 = x
	paths = []
	try:
		if a2 < 3:
			a2 = x/a2
			a2 = a2-0
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if q0 < 4:
			q0 = 6+q0
			paths.append(3)
		else:
			a2 = q0/7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		a2 = q0**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))