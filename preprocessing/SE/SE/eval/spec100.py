import numpy as np 

def function(x):

	q3 = 5
	e5 = 2
	x = x
	paths = []
	try:
		if x < 3:
			e5 = 0*8
			q3 = q3*4
			paths.append(1)
		else:
			e5 = e5+x
			q3 = 1-0
			q3 = q3-4
			paths.append(2)
		if e5 > 3:
			x = x-0
			q3 = q3/5
			e5 = e5-7
			paths.append(3)
		else:
			q3 = q3*4
			q3 = q3*q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		e5 = q3**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))