import numpy as np 

def function(x):

	u4 = 6
	q1 = x
	paths = []
	try:
		if u4 > 5:
			u4 = 5/6
			paths.append(1)
		else:
			x = x+x
			q1 = q1-9
			paths.append(2)
		if x >= 7:
			q1 = q1*8
			paths.append(3)
		else:
			x = x-2
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