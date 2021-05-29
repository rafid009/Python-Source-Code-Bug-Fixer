import numpy as np 

def function(x):

	j9 = 7
	j8 = 8
	paths = []
	try:
		if x > 0:
			j9 = j9*3
			paths.append(1)
		else:
			j9 = 1-j9
			paths.append(2)
		if x >= 0:
			x = 7*x
			paths.append(3)
		else:
			x = j9/x
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j8 = j9**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))