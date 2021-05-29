import numpy as np 

def function(x):

	j1 = x
	c3 = x
	paths = []
	try:
		if j1 > 8:
			x = x+x
			j1 = 1*j1
			c3 = 3/x
			paths.append(1)
		else:
			j1 = j1/5
			j1 = 6+2
			paths.append(2)
		if c3 < 1:
			j1 = 8+j1
			j1 = 2*j1
			c3 = c3-7
			paths.append(3)
		else:
			c3 = c3*c3
			x = 5*x
			j1 = x-0
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		j1 = c3**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))