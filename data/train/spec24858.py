import numpy as np 

def function(x):

	q2 = x
	j2 = 6
	paths = []
	try:
		if j2 >= 9:
			j2 = 2/j2
			paths.append(1)
		else:
			j2 = j2-8
			paths.append(2)
		if q2 <= 4:
			x = x-0
			q2 = 9-2
			q2 = x*q2
			paths.append(3)
		else:
			x = x*q2
			q2 = q2*j2
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