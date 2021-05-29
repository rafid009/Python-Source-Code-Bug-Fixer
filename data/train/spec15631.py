import numpy as np 

def function(x):

	i6 = 5
	q2 = 0
	x = 9
	paths = []
	try:
		if i6 >= 6:
			i6 = i6*i6
			q2 = x-4
			x = x-2
			paths.append(1)
		else:
			i6 = i6/8
			paths.append(2)
		if x >= 7:
			q2 = q2-i6
			paths.append(3)
		else:
			x = x+q2
			q2 = q2*4
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		i6 = q2**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))