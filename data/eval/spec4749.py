import numpy as np 

def function(x):

	j2 = 7
	x0 = 5
	paths = []
	try:
		if x0 < 1:
			x0 = 8/1
			x = x-1
			j2 = j2*9
			paths.append(1)
		else:
			x0 = 1+x0
			paths.append(2)
		if x <= 5:
			j2 = x0-j2
			paths.append(3)
		else:
			x = j2*3
			x0 = x0-9
			x0 = 0/x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))