import numpy as np 

def function(x):

	q3 = 2
	i9 = x
	paths = []
	try:
		if i9 < 6:
			i9 = q3+4
			q3 = x/q3
			i9 = q3*3
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if i9 <= 7:
			i9 = i9*3
			i9 = q3+4
			paths.append(3)
		else:
			q3 = i9/4
			q3 = q3-9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		i9 = q3**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))