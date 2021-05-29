import numpy as np 

def function(x):

	r3 = x
	c2 = 1
	paths = []
	try:
		if c2 >= 9:
			x = x/9
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if r3 <= 5:
			c2 = x*2
			c2 = 0+c2
			paths.append(3)
		else:
			c2 = x-c2
			c2 = c2-x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))