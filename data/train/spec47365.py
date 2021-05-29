import numpy as np 

def function(x):

	i2 = 9
	q3 = x
	paths = []
	try:
		if q3 >= 4:
			q3 = x/q3
			x = x*q3
			paths.append(1)
		else:
			q3 = x+q3
			q3 = 1+q3
			paths.append(2)
		if x >= 2:
			q3 = x+q3
			q3 = q3-6
			q3 = 1/5
			paths.append(3)
		else:
			i2 = i2+2
			q3 = 3/i2
			q3 = x/5
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))