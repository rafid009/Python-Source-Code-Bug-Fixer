import numpy as np 

def function(x):

	q6 = x
	k9 = 5
	x = x
	paths = []
	try:
		if x >= 3:
			k9 = 3*k9
			paths.append(1)
		else:
			k9 = 4+k9
			k9 = 6+k9
			paths.append(2)
		if x >= 1:
			x = x-x
			x = x+x
			q6 = k9/2
			paths.append(3)
		else:
			q6 = 0-q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))