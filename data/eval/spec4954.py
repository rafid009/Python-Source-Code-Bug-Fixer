import numpy as np 

def function(x):

	j6 = 1
	h9 = 5
	paths = []
	try:
		if x < 8:
			j6 = j6*5
			paths.append(1)
		else:
			j6 = j6*0
			j6 = j6-1
			x = x+1
			paths.append(2)
		if x > 0:
			x = x+3
			paths.append(3)
		else:
			h9 = h9*h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))