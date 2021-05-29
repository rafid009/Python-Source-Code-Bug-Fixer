import numpy as np 

def function(x):

	l1 = x
	j7 = 3
	x = x
	paths = []
	try:
		if x <= 5:
			j7 = j7/6
			l1 = 5/l1
			paths.append(1)
		else:
			x = x-1
			l1 = l1-7
			paths.append(2)
		if j7 < 3:
			j7 = x/7
			paths.append(3)
		else:
			l1 = 4/l1
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		l1 = j7**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))