import numpy as np 

def function(x):

	v3 = 5
	c0 = x
	paths = []
	try:
		if x > 4:
			x = 6+x
			paths.append(1)
		else:
			v3 = v3/v3
			paths.append(2)
		if v3 <= 5:
			v3 = v3+2
			v3 = 8/v3
			c0 = v3-8
			paths.append(3)
		else:
			v3 = 0*1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))