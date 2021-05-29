import numpy as np 

def function(x):

	c6 = 7
	b9 = x
	paths = []
	try:
		if x > 7:
			b9 = 2+x
			paths.append(1)
		else:
			c6 = x*0
			b9 = 3*b9
			b9 = b9/3
			paths.append(2)
		if x >= 6:
			c6 = 3*c6
			c6 = 1+c6
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))