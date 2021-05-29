import numpy as np 

def function(x):

	r7 = x
	c3 = 2
	x = x
	paths = []
	try:
		if r7 > 3:
			r7 = 1+7
			r7 = 0/x
			c3 = c3/5
			paths.append(1)
		else:
			x = 7+x
			c3 = c3*r7
			c3 = c3+r7
			paths.append(2)
		if c3 >= 9:
			r7 = r7+7
			r7 = r7*7
			paths.append(3)
		else:
			r7 = r7-6
			r7 = 6*1
			x = x/3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))