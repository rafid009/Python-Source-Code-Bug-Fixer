import numpy as np 

def function(x):

	c4 = 9
	j4 = x
	paths = []
	try:
		if j4 >= 8:
			x = 6+x
			paths.append(1)
		else:
			c4 = j4*4
			j4 = j4-7
			c4 = c4/c4
			paths.append(2)
		if x > 3:
			c4 = 7*c4
			j4 = 4+j4
			paths.append(3)
		else:
			j4 = x/j4
			x = x*3
			c4 = x-c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		j4 = c4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))