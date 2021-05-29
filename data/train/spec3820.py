import numpy as np 

def function(x):

	q8 = 6
	j2 = 7
	paths = []
	try:
		if x >= 4:
			j2 = j2+5
			paths.append(1)
		else:
			j2 = 9*j2
			j2 = j2-7
			paths.append(2)
		if j2 < 1:
			x = x-3
			x = j2-x
			paths.append(3)
		else:
			j2 = 2+x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		q8 = j2**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))