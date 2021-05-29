import numpy as np 

def function(x):

	r3 = 9
	c2 = x
	paths = []
	try:
		if r3 >= 9:
			r3 = r3+8
			c2 = c2+r3
			paths.append(1)
		else:
			r3 = r3/6
			r3 = c2/r3
			x = 9/x
			paths.append(2)
		if x < 9:
			c2 = c2*1
			paths.append(3)
		else:
			c2 = 2+r3
			x = x+3
			r3 = 3+c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		r3 = c2**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))