import numpy as np 

def function(x):

	q1 = x
	i4 = 9
	paths = []
	try:
		if i4 >= 6:
			q1 = 7/q1
			x = q1+x
			x = 9+x
			paths.append(1)
		else:
			q1 = 4*q1
			i4 = 7+q1
			q1 = 2*q1
			paths.append(2)
		if x <= 2:
			q1 = 8+q1
			i4 = q1+i4
			i4 = i4-i4
			paths.append(3)
		else:
			q1 = x/6
			i4 = i4-x
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))