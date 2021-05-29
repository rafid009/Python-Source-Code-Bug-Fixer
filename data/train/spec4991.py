import numpy as np 

def function(x):

	c5 = 3
	v6 = 1
	paths = []
	try:
		if c5 <= 6:
			x = v6+x
			v6 = 3/7
			paths.append(1)
		else:
			x = 2*x
			c5 = c5*x
			paths.append(2)
		if x < 4:
			v6 = 3+1
			v6 = 0*v6
			paths.append(3)
		else:
			c5 = c5*5
			c5 = 7-c5
			x = x+c5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))