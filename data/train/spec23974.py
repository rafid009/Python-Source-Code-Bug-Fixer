import numpy as np 

def function(x):

	j6 = 5
	c2 = 9
	paths = []
	try:
		if x >= 6:
			x = x+1
			x = c2*1
			paths.append(1)
		else:
			j6 = 5-j6
			c2 = c2*8
			paths.append(2)
		if x <= 0:
			c2 = 2/7
			j6 = j6/2
			paths.append(3)
		else:
			x = 2*x
			j6 = j6-4
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))