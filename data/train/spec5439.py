import numpy as np 

def function(x):

	v6 = 8
	c1 = x
	paths = []
	try:
		if c1 > 4:
			c1 = 1+c1
			x = x*5
			paths.append(1)
		else:
			c1 = 2/c1
			v6 = x+v6
			c1 = c1*3
			paths.append(2)
		if x <= 6:
			v6 = v6/7
			paths.append(3)
		else:
			c1 = c1/x
			x = 3*7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))