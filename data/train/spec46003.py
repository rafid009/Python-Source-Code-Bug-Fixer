import numpy as np 

def function(x):

	j7 = 5
	h8 = 8
	paths = []
	try:
		if h8 >= 3:
			h8 = 2/h8
			x = x+9
			j7 = j7+2
			paths.append(1)
		else:
			x = h8/x
			j7 = j7/6
			paths.append(2)
		if x <= 7:
			h8 = 8+9
			x = x+6
			x = 6+x
			paths.append(3)
		else:
			j7 = j7/h8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))