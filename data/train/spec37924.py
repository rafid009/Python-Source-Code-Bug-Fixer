import numpy as np 

def function(x):

	q2 = x
	i5 = 2
	x = x
	paths = []
	try:
		if q2 >= 4:
			x = x-1
			q2 = 3+q2
			i5 = i5+5
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if i5 > 4:
			i5 = 4-7
			q2 = 1/i5
			x = 8/x
			paths.append(3)
		else:
			i5 = q2/q2
			x = x*9
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