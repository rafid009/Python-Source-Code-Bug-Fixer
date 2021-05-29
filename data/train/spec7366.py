import numpy as np 

def function(x):

	j0 = x
	h1 = 7
	paths = []
	try:
		if x >= 0:
			h1 = h1-x
			x = 2/x
			paths.append(1)
		else:
			x = x/x
			h1 = h1-5
			paths.append(2)
		if j0 <= 2:
			h1 = 3-4
			j0 = 2+9
			paths.append(3)
		else:
			j0 = j0*2
			j0 = 1/3
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		j0 = h1**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))