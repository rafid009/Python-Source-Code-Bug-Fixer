import numpy as np 

def function(x):

	q0 = 3
	v5 = x
	paths = []
	try:
		if q0 < 2:
			v5 = v5*8
			q0 = v5*6
			paths.append(1)
		else:
			q0 = 5-q0
			paths.append(2)
		if x < 3:
			v5 = v5-0
			paths.append(3)
		else:
			q0 = q0/q0
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))