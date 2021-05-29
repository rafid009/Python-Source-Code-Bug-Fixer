import numpy as np 

def function(x):

	q5 = x
	j7 = 8
	paths = []
	try:
		if j7 <= 6:
			j7 = j7-x
			j7 = 2/3
			paths.append(1)
		else:
			q5 = q5*8
			paths.append(2)
		if j7 >= 0:
			x = q5-4
			q5 = 0-q5
			x = x-3
			paths.append(3)
		else:
			q5 = x-5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		j7 = q5**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))