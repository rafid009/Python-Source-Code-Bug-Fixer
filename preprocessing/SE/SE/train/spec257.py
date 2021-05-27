import numpy as np 

def function(x):

	j0 = 7
	c5 = x
	paths = []
	try:
		if j0 > 4:
			x = x*9
			paths.append(1)
		else:
			x = x/c5
			x = 9-0
			paths.append(2)
		if c5 <= 1:
			c5 = 2+c5
			x = c5*x
			c5 = c5*9
			paths.append(3)
		else:
			j0 = j0/j0
			j0 = 6+c5
			j0 = 1+j0
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		j0 = c5**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))