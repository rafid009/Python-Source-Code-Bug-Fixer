import numpy as np 

def function(x):

	n7 = 0
	q1 = x
	paths = []
	try:
		if n7 >= 9:
			x = 2-x
			q1 = n7+q1
			paths.append(1)
		else:
			n7 = n7*6
			n7 = 7*1
			paths.append(2)
		if n7 >= 3:
			n7 = x*8
			x = q1+x
			x = x/x
			paths.append(3)
		else:
			q1 = q1+7
			n7 = 6+4
			q1 = n7/9
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))