import numpy as np 

def function(x):

	j2 = x
	q4 = 9
	paths = []
	try:
		if q4 <= 4:
			x = 1*q4
			q4 = q4+q4
			paths.append(1)
		else:
			x = x/1
			j2 = j2*x
			paths.append(2)
		if q4 > 8:
			j2 = 3+q4
			paths.append(3)
		else:
			q4 = 0+0
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