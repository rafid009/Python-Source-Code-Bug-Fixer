import numpy as np 

def function(x):

	j1 = 6
	k4 = 2
	paths = []
	try:
		if x > 8:
			j1 = 7+8
			paths.append(1)
		else:
			j1 = 1*2
			k4 = j1*k4
			x = x/7
			paths.append(2)
		if j1 >= 4:
			x = x+2
			k4 = k4+1
			paths.append(3)
		else:
			k4 = k4+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))