import numpy as np 

def function(x):

	j5 = 1
	h6 = x
	paths = []
	try:
		if x >= 3:
			x = x*0
			paths.append(1)
		else:
			j5 = j5/5
			j5 = j5-7
			paths.append(2)
		if x < 3:
			h6 = x*h6
			paths.append(3)
		else:
			h6 = 8+h6
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))