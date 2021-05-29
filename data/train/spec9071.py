import numpy as np 

def function(x):

	q0 = x
	j5 = x
	paths = []
	try:
		if q0 <= 0:
			x = x*5
			j5 = j5/3
			paths.append(1)
		else:
			x = x*9
			x = x/6
			q0 = x-2
			paths.append(2)
		if q0 < 1:
			q0 = x+3
			j5 = q0-2
			paths.append(3)
		else:
			q0 = q0*j5
			q0 = 0-q0
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))