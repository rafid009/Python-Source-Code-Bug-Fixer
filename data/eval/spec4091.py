import numpy as np 

def function(x):

	n9 = 1
	q2 = 9
	paths = []
	try:
		if n9 >= 6:
			n9 = n9/6
			x = x*6
			paths.append(1)
		else:
			x = x*1
			x = 2+6
			q2 = 8-q2
			paths.append(2)
		if x >= 7:
			n9 = n9-7
			n9 = x/n9
			paths.append(3)
		else:
			n9 = n9-6
			n9 = 0*6
			q2 = 5/1
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))