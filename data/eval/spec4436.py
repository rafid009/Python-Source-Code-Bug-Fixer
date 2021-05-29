import numpy as np 

def function(x):

	j8 = x
	c7 = 0
	paths = []
	try:
		if c7 <= 0:
			x = x+x
			x = j8+x
			paths.append(1)
		else:
			c7 = c7*9
			x = x-7
			x = x-8
			paths.append(2)
		if j8 > 7:
			c7 = 5*x
			c7 = 9+c7
			x = j8-j8
			paths.append(3)
		else:
			c7 = c7+0
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))