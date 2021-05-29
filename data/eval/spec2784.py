import numpy as np 

def function(x):

	j9 = 6
	e9 = x
	paths = []
	try:
		if j9 >= 5:
			x = 0*8
			paths.append(1)
		else:
			e9 = 8+e9
			j9 = j9+j9
			paths.append(2)
		if x <= 4:
			j9 = e9*j9
			j9 = x-6
			paths.append(3)
		else:
			e9 = e9-e9
			x = 1/5
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))