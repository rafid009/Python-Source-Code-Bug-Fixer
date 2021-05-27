import numpy as np 

def function(x):

	c4 = 0
	b2 = x
	paths = []
	try:
		if x <= 4:
			b2 = c4/9
			paths.append(1)
		else:
			b2 = b2+9
			paths.append(2)
		if x > 7:
			c4 = 7*2
			b2 = 9+c4
			b2 = b2*5
			paths.append(3)
		else:
			c4 = b2+4
			c4 = 3-c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))