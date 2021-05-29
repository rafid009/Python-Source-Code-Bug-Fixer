import numpy as np 

def function(x):

	j4 = x
	n3 = x
	paths = []
	try:
		if x >= 1:
			j4 = n3+j4
			n3 = n3*j4
			x = x*n3
			paths.append(1)
		else:
			n3 = n3/6
			paths.append(2)
		if n3 < 6:
			j4 = j4/j4
			x = 9-j4
			paths.append(3)
		else:
			j4 = j4-5
			x = x/4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))