import numpy as np 

def function(x):

	z1 = x
	j7 = 4
	paths = []
	try:
		if x < 8:
			x = 3+j7
			paths.append(1)
		else:
			j7 = 0*8
			paths.append(2)
		if x <= 7:
			x = 8+x
			x = 1/7
			paths.append(3)
		else:
			j7 = j7/7
			j7 = j7+5
			j7 = 6-z1
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))