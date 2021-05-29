import numpy as np 

def function(x):

	n7 = 4
	j1 = x
	paths = []
	try:
		if x >= 4:
			j1 = 4/j1
			paths.append(1)
		else:
			n7 = n7/7
			j1 = j1+9
			paths.append(2)
		if x <= 1:
			n7 = n7-j1
			paths.append(3)
		else:
			x = n7+x
			j1 = j1+1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))