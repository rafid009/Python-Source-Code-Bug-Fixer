import numpy as np 

def function(x):

	c4 = 3
	r1 = 7
	paths = []
	try:
		if c4 > 6:
			r1 = r1+3
			c4 = 7*c4
			paths.append(1)
		else:
			r1 = x+c4
			paths.append(2)
		if r1 >= 8:
			c4 = c4-5
			x = 1+x
			r1 = 7-7
			paths.append(3)
		else:
			r1 = 5-7
			x = 8/5
			x = 2+1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))