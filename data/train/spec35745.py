import numpy as np 

def function(x):

	j3 = x
	e9 = 3
	paths = []
	try:
		if j3 > 4:
			e9 = e9+0
			e9 = e9+8
			paths.append(1)
		else:
			j3 = 9*j3
			j3 = j3/e9
			x = j3/3
			paths.append(2)
		if e9 >= 1:
			j3 = j3+9
			e9 = e9+e9
			paths.append(3)
		else:
			e9 = e9-4
			x = x-3
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