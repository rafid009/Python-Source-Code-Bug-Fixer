import numpy as np 

def function(x):

	k4 = x
	j9 = x
	paths = []
	try:
		if j9 <= 4:
			j9 = 6-k4
			k4 = k4/1
			paths.append(1)
		else:
			j9 = 6*j9
			k4 = 7+j9
			k4 = k4/x
			paths.append(2)
		if j9 > 2:
			j9 = j9+9
			paths.append(3)
		else:
			j9 = j9/4
			x = 6-k4
			k4 = k4*0
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