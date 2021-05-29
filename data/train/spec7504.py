import numpy as np 

def function(x):

	k4 = 7
	j1 = x
	paths = []
	try:
		if k4 < 9:
			x = x-x
			paths.append(1)
		else:
			j1 = 9*x
			j1 = 4-5
			j1 = j1+x
			paths.append(2)
		if j1 > 1:
			x = x+9
			k4 = 7/k4
			k4 = 1-8
			paths.append(3)
		else:
			k4 = 7+1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		k4 = j1**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))