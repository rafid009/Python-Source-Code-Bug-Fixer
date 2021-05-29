import numpy as np 

def function(x):

	j5 = x
	h1 = x
	paths = []
	try:
		if h1 <= 3:
			h1 = x+h1
			h1 = 2+h1
			paths.append(1)
		else:
			h1 = h1+4
			j5 = j5*2
			paths.append(2)
		if x >= 3:
			h1 = h1/6
			paths.append(3)
		else:
			h1 = j5-3
			j5 = j5/2
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