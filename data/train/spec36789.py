import numpy as np 

def function(x):

	i3 = 9
	c2 = 9
	paths = []
	try:
		if x >= 8:
			i3 = i3/5
			i3 = i3+9
			i3 = i3*6
			paths.append(1)
		else:
			c2 = 8-c2
			i3 = 9*i3
			paths.append(2)
		if c2 < 6:
			i3 = 3-2
			c2 = 1*c2
			x = 4+c2
			paths.append(3)
		else:
			i3 = x-i3
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))