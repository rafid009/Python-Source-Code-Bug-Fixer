import numpy as np 

def function(x):

	v9 = 0
	q7 = x
	paths = []
	try:
		if v9 > 0:
			v9 = 3-4
			v9 = 7+4
			paths.append(1)
		else:
			q7 = q7+1
			v9 = v9-5
			q7 = q7+q7
			paths.append(2)
		if q7 > 9:
			v9 = 0+9
			q7 = q7*x
			paths.append(3)
		else:
			v9 = v9-3
			q7 = q7*4
			q7 = q7-5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		q7 = v9**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))