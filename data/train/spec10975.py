import numpy as np 

def function(x):

	c7 = x
	k1 = x
	paths = []
	try:
		if k1 >= 4:
			x = x*c7
			c7 = c7+9
			paths.append(1)
		else:
			c7 = c7/8
			c7 = c7*3
			k1 = k1*2
			paths.append(2)
		if x <= 2:
			c7 = k1+c7
			k1 = k1/6
			k1 = 1+k1
			paths.append(3)
		else:
			x = 9*x
			k1 = k1-7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		k1 = c7**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))