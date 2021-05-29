import numpy as np 

def function(x):

	j8 = x
	c2 = x
	paths = []
	try:
		if j8 >= 0:
			x = x*c2
			paths.append(1)
		else:
			c2 = j8-6
			j8 = c2/j8
			x = x+4
			paths.append(2)
		if x > 5:
			x = 5+x
			c2 = 8+x
			x = x*0
			paths.append(3)
		else:
			c2 = c2-5
			c2 = 6/x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		j8 = c2**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))