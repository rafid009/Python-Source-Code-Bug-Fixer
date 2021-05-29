import numpy as np 

def function(x):

	c5 = 2
	v0 = 3
	paths = []
	try:
		if v0 >= 1:
			c5 = c5-5
			paths.append(1)
		else:
			c5 = c5/7
			c5 = c5+1
			paths.append(2)
		if x <= 1:
			c5 = v0+v0
			v0 = v0*2
			x = x*0
			paths.append(3)
		else:
			v0 = 1/v0
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