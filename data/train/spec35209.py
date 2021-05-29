import numpy as np 

def function(x):

	q8 = 6
	j9 = x
	paths = []
	try:
		if q8 > 1:
			x = x/5
			paths.append(1)
		else:
			j9 = j9*q8
			j9 = j9/1
			paths.append(2)
		if x <= 1:
			j9 = x-x
			paths.append(3)
		else:
			j9 = 4-6
			j9 = j9*4
			q8 = q8+9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))