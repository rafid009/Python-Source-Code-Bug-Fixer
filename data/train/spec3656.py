import numpy as np 

def function(x):

	q1 = 9
	j2 = x
	paths = []
	try:
		if q1 >= 5:
			x = x+8
			paths.append(1)
		else:
			q1 = q1+8
			paths.append(2)
		if q1 >= 0:
			x = x/7
			x = x*q1
			j2 = j2-q1
			paths.append(3)
		else:
			q1 = q1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))