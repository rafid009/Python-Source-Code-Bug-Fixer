import numpy as np 

def function(x):

	q0 = x
	j7 = x
	paths = []
	try:
		if q0 < 4:
			q0 = 8*q0
			x = q0*x
			paths.append(1)
		else:
			j7 = j7-6
			j7 = 0+2
			paths.append(2)
		if j7 > 1:
			x = x/3
			j7 = j7*3
			x = x-1
			paths.append(3)
		else:
			x = 5*7
			x = x/4
			q0 = x+2
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		q0 = j7**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))