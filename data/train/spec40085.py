import numpy as np 

def function(x):

	j7 = x
	n1 = x
	x = 1
	paths = []
	try:
		if j7 < 9:
			j7 = 2+j7
			n1 = 1-n1
			n1 = 6-3
			paths.append(1)
		else:
			j7 = j7-3
			n1 = n1*1
			x = x-1
			paths.append(2)
		if n1 > 1:
			n1 = n1-6
			x = n1-2
			n1 = n1-1
			paths.append(3)
		else:
			j7 = j7+j7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))