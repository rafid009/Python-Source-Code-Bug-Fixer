import numpy as np 

def function(x):

	q2 = x
	j6 = 4
	paths = []
	try:
		if j6 < 3:
			j6 = q2/j6
			paths.append(1)
		else:
			q2 = 8*q2
			x = 3+x
			q2 = q2-3
			paths.append(2)
		if x > 5:
			j6 = q2*7
			q2 = 7/q2
			paths.append(3)
		else:
			j6 = j6-j6
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