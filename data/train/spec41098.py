import numpy as np 

def function(x):

	u2 = 4
	j9 = x
	x = 2
	paths = []
	try:
		if x > 9:
			j9 = j9/2
			j9 = j9/j9
			paths.append(1)
		else:
			u2 = u2/x
			x = 6+2
			paths.append(2)
		if x <= 5:
			j9 = 0-x
			u2 = 0/j9
			j9 = u2*j9
			paths.append(3)
		else:
			u2 = x/u2
			x = x-4
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))