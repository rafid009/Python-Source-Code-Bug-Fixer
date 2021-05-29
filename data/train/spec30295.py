import numpy as np 

def function(x):

	v0 = x
	c2 = 8
	paths = []
	try:
		if v0 <= 8:
			c2 = 2/8
			v0 = v0*x
			c2 = c2/6
			paths.append(1)
		else:
			c2 = 6+c2
			x = 7*8
			paths.append(2)
		if c2 >= 5:
			c2 = 2+0
			v0 = v0+9
			x = x/v0
			paths.append(3)
		else:
			v0 = 8*v0
			x = c2+x
			v0 = v0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))