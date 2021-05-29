import numpy as np 

def function(x):

	q0 = x
	f7 = 8
	paths = []
	try:
		if x > 9:
			f7 = f7/3
			q0 = q0+f7
			q0 = 6-9
			paths.append(1)
		else:
			x = x+8
			x = x*5
			paths.append(2)
		if x < 8:
			f7 = f7/4
			paths.append(3)
		else:
			q0 = q0-5
			q0 = q0-f7
			x = x+9
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