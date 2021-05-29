import numpy as np 

def function(x):

	p3 = x
	c7 = x
	paths = []
	try:
		if x >= 7:
			x = 1+x
			x = x+c7
			x = 6-x
			paths.append(1)
		else:
			x = 4/3
			c7 = c7-p3
			c7 = c7-p3
			paths.append(2)
		if x > 9:
			p3 = x*1
			p3 = p3+9
			c7 = 5-c7
			paths.append(3)
		else:
			p3 = 3+1
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))