import numpy as np 

def function(x):

	q1 = x
	i2 = 4
	paths = []
	try:
		if x <= 2:
			q1 = 0-q1
			x = 2+x
			i2 = 9+8
			paths.append(1)
		else:
			x = 1+6
			q1 = x+x
			i2 = i2/i2
			paths.append(2)
		if i2 >= 4:
			x = x*7
			paths.append(3)
		else:
			q1 = 5-q1
			q1 = x+9
			i2 = i2-q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))