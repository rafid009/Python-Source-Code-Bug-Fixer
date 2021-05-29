import numpy as np 

def function(x):

	j7 = x
	q6 = 3
	paths = []
	try:
		if j7 > 2:
			q6 = q6*1
			paths.append(1)
		else:
			q6 = j7+q6
			j7 = 8*x
			paths.append(2)
		if x >= 2:
			j7 = j7*0
			j7 = 9*2
			q6 = q6*6
			paths.append(3)
		else:
			q6 = q6/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))