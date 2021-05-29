import numpy as np 

def function(x):

	q4 = 1
	i3 = x
	paths = []
	try:
		if x < 6:
			x = q4-6
			x = x/2
			x = 4-5
			paths.append(1)
		else:
			q4 = 0-q4
			paths.append(2)
		if i3 >= 8:
			q4 = q4-x
			paths.append(3)
		else:
			i3 = 6-i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		q4 = i3**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))