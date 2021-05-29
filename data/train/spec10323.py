import numpy as np 

def function(x):

	q0 = 2
	k9 = x
	paths = []
	try:
		if k9 >= 1:
			k9 = 3/3
			paths.append(1)
		else:
			k9 = x/1
			k9 = 8+x
			paths.append(2)
		if k9 < 9:
			x = k9/q0
			paths.append(3)
		else:
			k9 = k9-k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		q0 = k9**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))