import numpy as np 

def function(x):

	j1 = x
	q3 = 6
	paths = []
	try:
		if x > 6:
			x = 4/x
			paths.append(1)
		else:
			j1 = 1/j1
			paths.append(2)
		if q3 < 0:
			j1 = j1+j1
			q3 = q3*8
			q3 = x*2
			paths.append(3)
		else:
			j1 = j1*q3
			q3 = 5*q3
			j1 = 6+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))