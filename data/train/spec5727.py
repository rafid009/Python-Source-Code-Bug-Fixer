import numpy as np 

def function(x):

	q2 = 5
	i2 = 2
	paths = []
	try:
		if i2 < 1:
			i2 = x+2
			i2 = i2-x
			i2 = i2*2
			paths.append(1)
		else:
			x = x/q2
			paths.append(2)
		if i2 >= 3:
			x = i2*x
			q2 = 7*2
			x = 3/x
			paths.append(3)
		else:
			i2 = 3+x
			q2 = q2-2
			q2 = x*q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))