import numpy as np 

def function(x):

	h4 = x
	j7 = 0
	x = 4
	paths = []
	try:
		if h4 >= 5:
			j7 = 5-j7
			paths.append(1)
		else:
			x = 9*3
			j7 = 3+j7
			paths.append(2)
		if h4 > 9:
			x = x/7
			j7 = 1/2
			x = h4+1
			paths.append(3)
		else:
			x = x*j7
			h4 = 0+h4
			j7 = j7-5
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))