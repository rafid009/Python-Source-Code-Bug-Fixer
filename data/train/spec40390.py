import numpy as np 

def function(x):

	j4 = 8
	j2 = x
	paths = []
	try:
		if j2 <= 3:
			j4 = 9+9
			paths.append(1)
		else:
			j2 = 0+j4
			paths.append(2)
		if x >= 1:
			j4 = j4*j4
			j4 = j2/x
			paths.append(3)
		else:
			x = 2-9
			x = x-2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))