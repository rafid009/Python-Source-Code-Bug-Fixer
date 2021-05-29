import numpy as np 

def function(x):

	h1 = x
	j5 = 4
	paths = []
	try:
		if j5 <= 3:
			x = 8*x
			paths.append(1)
		else:
			x = x*j5
			j5 = j5*x
			paths.append(2)
		if x >= 2:
			x = 1-x
			x = 7+x
			h1 = 4+8
			paths.append(3)
		else:
			j5 = 9/j5
			h1 = h1*5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))