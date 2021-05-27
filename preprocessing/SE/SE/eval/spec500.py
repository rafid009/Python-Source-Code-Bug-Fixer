import numpy as np 

def function(x):

	j2 = 1
	q7 = 1
	paths = []
	try:
		if j2 <= 2:
			j2 = x+j2
			paths.append(1)
		else:
			x = x*4
			j2 = q7-3
			q7 = x+5
			paths.append(2)
		if q7 >= 4:
			x = 3-x
			paths.append(3)
		else:
			x = j2+j2
			x = 1+j2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))