import numpy as np 

def function(x):

	j2 = x
	c3 = x
	paths = []
	try:
		if j2 < 3:
			c3 = c3*8
			c3 = 7+8
			c3 = c3-3
			paths.append(1)
		else:
			j2 = j2+j2
			c3 = x*j2
			x = x-6
			paths.append(2)
		if j2 > 1:
			j2 = 8*j2
			j2 = c3*j2
			paths.append(3)
		else:
			c3 = 2*x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))