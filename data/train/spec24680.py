import numpy as np 

def function(x):

	j3 = 8
	a2 = x
	paths = []
	try:
		if j3 <= 2:
			j3 = 5+4
			a2 = a2-6
			paths.append(1)
		else:
			a2 = a2-0
			a2 = a2-4
			a2 = 9+9
			paths.append(2)
		if a2 < 7:
			x = x-x
			paths.append(3)
		else:
			j3 = j3*a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))