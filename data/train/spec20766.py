import numpy as np 

def function(x):

	r5 = x
	c6 = 2
	paths = []
	try:
		if r5 < 1:
			x = 1*8
			r5 = r5*9
			paths.append(1)
		else:
			r5 = 4+5
			c6 = c6*2
			paths.append(2)
		if x >= 4:
			c6 = x*c6
			paths.append(3)
		else:
			x = 2-1
			x = x-7
			r5 = c6*c6
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