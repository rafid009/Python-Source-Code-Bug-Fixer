import numpy as np 

def function(x):

	i0 = 8
	q3 = 5
	paths = []
	try:
		if i0 <= 4:
			x = x*q3
			i0 = 6*6
			paths.append(1)
		else:
			x = 3-x
			i0 = 6+i0
			i0 = 6-i0
			paths.append(2)
		if i0 >= 2:
			i0 = i0/q3
			q3 = x/q3
			paths.append(3)
		else:
			q3 = i0-q3
			i0 = x*i0
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))