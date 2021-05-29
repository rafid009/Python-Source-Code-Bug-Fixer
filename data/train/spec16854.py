import numpy as np 

def function(x):

	n7 = 8
	j1 = 9
	paths = []
	try:
		if x < 3:
			j1 = j1*x
			n7 = n7/x
			j1 = j1*8
			paths.append(1)
		else:
			j1 = 6-6
			paths.append(2)
		if n7 < 6:
			j1 = j1+1
			paths.append(3)
		else:
			j1 = 7-7
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