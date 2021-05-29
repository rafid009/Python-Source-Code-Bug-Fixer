import numpy as np 

def function(x):

	j9 = 8
	e0 = x
	paths = []
	try:
		if j9 <= 4:
			j9 = j9*j9
			paths.append(1)
		else:
			j9 = 5/e0
			e0 = 1+e0
			e0 = x*1
			paths.append(2)
		if j9 >= 8:
			x = 2+1
			x = e0-x
			paths.append(3)
		else:
			x = 3*9
			j9 = j9+1
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))