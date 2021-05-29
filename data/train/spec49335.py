import numpy as np 

def function(x):

	l2 = 0
	j3 = x
	paths = []
	try:
		if j3 > 2:
			x = 1-9
			l2 = 6+6
			paths.append(1)
		else:
			x = x-0
			j3 = 9/3
			paths.append(2)
		if l2 <= 7:
			j3 = j3/x
			paths.append(3)
		else:
			x = x+l2
			j3 = 1-1
			x = 6/4
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		l2 = j3**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))