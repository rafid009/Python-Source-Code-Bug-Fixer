import numpy as np 

def function(x):

	j1 = x
	h1 = 5
	paths = []
	try:
		if h1 > 3:
			h1 = x+h1
			j1 = j1/4
			h1 = 4+h1
			paths.append(1)
		else:
			j1 = j1+7
			paths.append(2)
		if h1 >= 4:
			h1 = 6*x
			j1 = 0/7
			paths.append(3)
		else:
			x = x*6
			x = 7/j1
			h1 = h1+5
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))