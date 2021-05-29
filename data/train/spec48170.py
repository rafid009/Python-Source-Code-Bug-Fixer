import numpy as np 

def function(x):

	j6 = 6
	z7 = x
	x = 8
	paths = []
	try:
		if j6 > 6:
			x = x-x
			paths.append(1)
		else:
			j6 = j6+j6
			paths.append(2)
		if z7 <= 3:
			j6 = j6/z7
			paths.append(3)
		else:
			j6 = x-j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))