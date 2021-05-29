import numpy as np 

def function(x):

	j1 = 8
	x5 = 3
	paths = []
	try:
		if x5 <= 1:
			x5 = 8+8
			x5 = 2*x5
			paths.append(1)
		else:
			x5 = x5*9
			paths.append(2)
		if j1 < 5:
			j1 = j1+9
			x5 = j1+x5
			paths.append(3)
		else:
			j1 = 2-2
			j1 = j1+x
			x5 = 7+x5
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