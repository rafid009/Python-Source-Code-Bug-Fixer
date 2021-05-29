import numpy as np 

def function(x):

	c9 = x
	j3 = x
	paths = []
	try:
		if j3 > 5:
			j3 = j3/c9
			c9 = c9-6
			j3 = 1-2
			paths.append(1)
		else:
			c9 = c9/7
			x = x+1
			paths.append(2)
		if c9 > 3:
			x = x+x
			x = x*9
			paths.append(3)
		else:
			c9 = 3/5
			c9 = c9/j3
			x = 4-9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))