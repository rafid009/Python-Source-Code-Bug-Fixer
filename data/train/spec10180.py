import numpy as np 

def function(x):

	c1 = x
	v1 = x
	paths = []
	try:
		if x > 1:
			x = v1-8
			v1 = v1/v1
			c1 = c1+5
			paths.append(1)
		else:
			v1 = v1-3
			x = x-4
			v1 = 5-v1
			paths.append(2)
		if c1 <= 4:
			c1 = c1+7
			x = 4*x
			paths.append(3)
		else:
			c1 = c1*7
			c1 = c1*1
			x = x*2
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))