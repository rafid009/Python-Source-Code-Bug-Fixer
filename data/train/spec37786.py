import numpy as np 

def function(x):

	h2 = x
	j8 = 0
	x = 0
	paths = []
	try:
		if h2 <= 4:
			x = x*6
			j8 = j8+h2
			paths.append(1)
		else:
			j8 = j8-3
			h2 = 3+0
			h2 = 2-h2
			paths.append(2)
		if h2 >= 5:
			j8 = 0-j8
			x = x-1
			h2 = x*h2
			paths.append(3)
		else:
			h2 = x-h2
			x = x+9
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))