import numpy as np 

def function(x):

	i5 = 7
	q6 = x
	paths = []
	try:
		if x < 9:
			i5 = 8*i5
			q6 = i5/q6
			i5 = i5*q6
			paths.append(1)
		else:
			x = x-7
			x = x/2
			i5 = i5-0
			paths.append(2)
		if x >= 2:
			x = q6*i5
			i5 = x*q6
			paths.append(3)
		else:
			i5 = q6*x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		i5 = q6**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))