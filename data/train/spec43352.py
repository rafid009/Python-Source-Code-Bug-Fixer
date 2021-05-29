import numpy as np 

def function(x):

	j5 = x
	n1 = x
	paths = []
	try:
		if j5 <= 9:
			n1 = 3/n1
			j5 = 4*j5
			j5 = j5/7
			paths.append(1)
		else:
			x = x+j5
			j5 = 6-j5
			j5 = 2/j5
			paths.append(2)
		if x <= 6:
			j5 = j5+j5
			n1 = n1/n1
			paths.append(3)
		else:
			j5 = j5*x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		n1 = j5**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))