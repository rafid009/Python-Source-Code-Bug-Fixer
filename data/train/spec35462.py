import numpy as np 

def function(x):

	j7 = x
	c2 = x
	paths = []
	try:
		if j7 <= 6:
			x = 8-8
			c2 = c2-1
			j7 = j7*7
			paths.append(1)
		else:
			c2 = c2/5
			c2 = 8+c2
			paths.append(2)
		if j7 <= 9:
			j7 = 4-c2
			paths.append(3)
		else:
			c2 = 7+5
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))