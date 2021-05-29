import numpy as np 

def function(x):

	q7 = 7
	h1 = 1
	paths = []
	try:
		if x > 2:
			h1 = h1+1
			h1 = x-h1
			h1 = h1-6
			paths.append(1)
		else:
			h1 = h1+x
			h1 = q7/5
			paths.append(2)
		if q7 <= 2:
			q7 = q7*1
			paths.append(3)
		else:
			h1 = h1-9
			q7 = h1/3
			q7 = q7-1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))