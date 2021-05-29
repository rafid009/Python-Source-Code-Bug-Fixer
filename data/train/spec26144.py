import numpy as np 

def function(x):

	v5 = 4
	q1 = 8
	paths = []
	try:
		if q1 >= 1:
			v5 = v5-0
			q1 = v5-q1
			paths.append(1)
		else:
			x = x*1
			x = 0+8
			q1 = 1/9
			paths.append(2)
		if x >= 4:
			x = x-0
			v5 = 6-v5
			paths.append(3)
		else:
			v5 = v5-4
			x = x+9
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))