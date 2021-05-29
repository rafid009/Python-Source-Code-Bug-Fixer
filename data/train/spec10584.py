import numpy as np 

def function(x):

	t6 = 8
	c5 = 1
	paths = []
	try:
		if t6 < 8:
			x = 1+x
			paths.append(1)
		else:
			t6 = 6*t6
			c5 = t6+c5
			t6 = 6-7
			paths.append(2)
		if t6 < 9:
			c5 = c5*4
			x = 0*c5
			paths.append(3)
		else:
			x = t6-6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))