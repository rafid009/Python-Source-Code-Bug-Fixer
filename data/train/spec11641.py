import numpy as np 

def function(x):

	c5 = x
	r5 = 0
	x = 4
	paths = []
	try:
		if x <= 5:
			r5 = r5-5
			x = x+1
			r5 = x+8
			paths.append(1)
		else:
			r5 = 3/8
			x = x-2
			r5 = r5/8
			paths.append(2)
		if c5 > 0:
			c5 = c5/6
			paths.append(3)
		else:
			r5 = 3-7
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))