import numpy as np 

def function(x):

	c1 = x
	d5 = 0
	paths = []
	try:
		if d5 > 8:
			x = x*0
			c1 = c1+x
			paths.append(1)
		else:
			c1 = c1/3
			paths.append(2)
		if d5 <= 8:
			x = c1+7
			x = 5+x
			d5 = 3+d5
			paths.append(3)
		else:
			d5 = d5+d5
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))