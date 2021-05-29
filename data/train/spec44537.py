import numpy as np 

def function(x):

	l2 = x
	j6 = 5
	paths = []
	try:
		if x >= 2:
			x = 4/x
			l2 = j6+l2
			paths.append(1)
		else:
			j6 = 4/x
			paths.append(2)
		if j6 > 7:
			j6 = j6+l2
			paths.append(3)
		else:
			x = x+3
			j6 = j6-9
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