import numpy as np 

def function(x):

	c2 = 4
	v6 = 7
	paths = []
	try:
		if x < 4:
			x = c2-5
			paths.append(1)
		else:
			c2 = c2-5
			x = 4+x
			c2 = c2-8
			paths.append(2)
		if c2 < 3:
			x = 7*5
			x = 1+3
			v6 = v6*0
			paths.append(3)
		else:
			x = x-9
			x = x*x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		v6 = c2**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))