import numpy as np 

def function(x):

	n5 = x
	q4 = x
	paths = []
	try:
		if x <= 2:
			q4 = 1-6
			q4 = q4+q4
			paths.append(1)
		else:
			n5 = n5+2
			x = n5/1
			x = x*0
			paths.append(2)
		if x >= 4:
			x = 7-q4
			x = x+n5
			paths.append(3)
		else:
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))