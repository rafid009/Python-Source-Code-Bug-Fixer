import numpy as np 

def function(x):

	j2 = 7
	k4 = 7
	x = 3
	paths = []
	try:
		if x >= 6:
			j2 = 7*k4
			j2 = j2*j2
			j2 = 6/x
			paths.append(1)
		else:
			j2 = 4-1
			paths.append(2)
		if x <= 2:
			j2 = 9-j2
			k4 = 8+2
			paths.append(3)
		else:
			k4 = 5+x
			x = 3-k4
			j2 = j2/x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		k4 = j2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))