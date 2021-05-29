import numpy as np 

def function(x):

	n1 = x
	j6 = 0
	paths = []
	try:
		if n1 > 6:
			n1 = n1+2
			n1 = n1*n1
			j6 = x+0
			paths.append(1)
		else:
			j6 = 6*n1
			paths.append(2)
		if x > 0:
			n1 = x+8
			paths.append(3)
		else:
			j6 = 6-4
			n1 = n1-5
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))