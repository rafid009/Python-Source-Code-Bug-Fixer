import numpy as np 

def function(x):

	j4 = 1
	q9 = 4
	x = x
	paths = []
	try:
		if q9 > 4:
			j4 = 7+x
			j4 = x*j4
			paths.append(1)
		else:
			x = 7+2
			paths.append(2)
		if j4 >= 1:
			x = x+x
			j4 = j4+4
			q9 = 6-x
			paths.append(3)
		else:
			j4 = 3*1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))