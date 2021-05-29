import numpy as np 

def function(x):

	q0 = 5
	p7 = 8
	paths = []
	try:
		if q0 >= 4:
			p7 = 9-x
			paths.append(1)
		else:
			x = x-x
			x = x/q0
			p7 = 2-4
			paths.append(2)
		if p7 <= 8:
			x = 9-x
			paths.append(3)
		else:
			q0 = q0-9
			p7 = p7/2
			p7 = 4*p7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))