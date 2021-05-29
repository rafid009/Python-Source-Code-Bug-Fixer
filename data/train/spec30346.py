import numpy as np 

def function(x):

	c5 = x
	r6 = x
	paths = []
	try:
		if c5 > 6:
			r6 = x+4
			paths.append(1)
		else:
			r6 = x*1
			r6 = 5-9
			paths.append(2)
		if x > 0:
			x = x+5
			c5 = c5/8
			r6 = 5*3
			paths.append(3)
		else:
			r6 = r6-6
			x = r6/x
			x = r6+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		r6 = c5**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))