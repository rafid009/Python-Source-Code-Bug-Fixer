import numpy as np 

def function(x):

	h4 = 6
	e9 = x
	x = x
	paths = []
	try:
		if h4 > 6:
			x = x/5
			x = x*9
			paths.append(1)
		else:
			h4 = 4/h4
			x = x+x
			paths.append(2)
		if x < 2:
			e9 = 6-e9
			h4 = h4+3
			e9 = 0-7
			paths.append(3)
		else:
			e9 = e9-6
			h4 = e9/9
			h4 = 0/h4
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))