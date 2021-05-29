import numpy as np 

def function(x):

	j1 = x
	b4 = 6
	x = x
	paths = []
	try:
		if x < 4:
			x = x/x
			j1 = j1/8
			j1 = 4-3
			paths.append(1)
		else:
			b4 = 3-b4
			paths.append(2)
		if x > 5:
			b4 = b4-9
			paths.append(3)
		else:
			x = x/6
			j1 = b4*6
			j1 = j1+3
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		j1 = b4**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))