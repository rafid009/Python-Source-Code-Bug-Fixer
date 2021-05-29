import numpy as np 

def function(x):

	n1 = 4
	j7 = 6
	paths = []
	try:
		if x < 2:
			x = 8+j7
			j7 = 8-8
			paths.append(1)
		else:
			x = x-4
			n1 = 6*j7
			j7 = n1-5
			paths.append(2)
		if n1 <= 5:
			j7 = j7-3
			paths.append(3)
		else:
			j7 = j7*1
			x = x-7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		n1 = j7**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))