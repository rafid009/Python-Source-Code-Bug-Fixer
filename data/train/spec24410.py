import numpy as np 

def function(x):

	n3 = x
	j0 = 8
	paths = []
	try:
		if n3 <= 0:
			x = x-7
			n3 = n3-n3
			paths.append(1)
		else:
			x = 7+x
			x = x-8
			paths.append(2)
		if x > 1:
			j0 = 6*j0
			j0 = 6/4
			paths.append(3)
		else:
			j0 = j0*9
			n3 = n3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))