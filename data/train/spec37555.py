import numpy as np 

def function(x):

	j9 = x
	c3 = x
	paths = []
	try:
		if x > 7:
			c3 = 2+1
			c3 = 7-c3
			paths.append(1)
		else:
			c3 = j9/3
			paths.append(2)
		if c3 > 7:
			x = 9/x
			paths.append(3)
		else:
			j9 = c3+c3
			x = x/2
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))