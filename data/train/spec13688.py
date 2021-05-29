import numpy as np 

def function(x):

	j2 = 7
	e7 = x
	paths = []
	try:
		if e7 <= 9:
			e7 = 1-e7
			paths.append(1)
		else:
			j2 = 0-j2
			x = x*e7
			paths.append(2)
		if j2 <= 4:
			x = x-7
			paths.append(3)
		else:
			j2 = 8*j2
			e7 = 6/e7
			x = x/e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))