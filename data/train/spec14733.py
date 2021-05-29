import numpy as np 

def function(x):

	j3 = 7
	n1 = 2
	paths = []
	try:
		if x < 3:
			n1 = 3*5
			j3 = 1-n1
			j3 = j3-0
			paths.append(1)
		else:
			n1 = j3-n1
			paths.append(2)
		if j3 < 1:
			j3 = j3-n1
			j3 = x/x
			paths.append(3)
		else:
			x = x*x
			n1 = x/n1
			j3 = j3/n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))