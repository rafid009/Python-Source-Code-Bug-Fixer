import numpy as np 

def function(x):

	k1 = 4
	q4 = x
	paths = []
	try:
		if x >= 9:
			k1 = 0-x
			q4 = 0/q4
			paths.append(1)
		else:
			k1 = k1-8
			q4 = q4/q4
			k1 = 0-k1
			paths.append(2)
		if x < 6:
			x = x/7
			q4 = q4+k1
			k1 = k1-3
			paths.append(3)
		else:
			q4 = k1*2
			q4 = k1+q4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		q4 = k1**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))