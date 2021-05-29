import numpy as np 

def function(x):

	j3 = 9
	e5 = 9
	paths = []
	try:
		if e5 <= 2:
			x = x+9
			j3 = j3*j3
			paths.append(1)
		else:
			x = 6-e5
			paths.append(2)
		if j3 > 7:
			e5 = e5-e5
			paths.append(3)
		else:
			j3 = 0*j3
			j3 = j3-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))