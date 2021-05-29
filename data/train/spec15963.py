import numpy as np 

def function(x):

	j6 = 5
	n0 = 9
	x = x
	paths = []
	try:
		if x > 8:
			x = n0-j6
			paths.append(1)
		else:
			n0 = n0-4
			j6 = j6*x
			n0 = 6+4
			paths.append(2)
		if j6 < 8:
			n0 = n0/5
			x = 4+x
			n0 = x*n0
			paths.append(3)
		else:
			x = 3-x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		j6 = n0**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))