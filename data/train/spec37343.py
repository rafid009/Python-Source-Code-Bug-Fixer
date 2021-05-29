import numpy as np 

def function(x):

	u3 = 4
	q3 = 8
	paths = []
	try:
		if x >= 6:
			x = 7+x
			x = x*9
			paths.append(1)
		else:
			u3 = u3+5
			paths.append(2)
		if x >= 3:
			u3 = 6-u3
			q3 = q3+4
			paths.append(3)
		else:
			q3 = u3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))