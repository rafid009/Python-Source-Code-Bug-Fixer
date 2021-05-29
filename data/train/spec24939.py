import numpy as np 

def function(x):

	q5 = x
	n4 = x
	paths = []
	try:
		if x > 8:
			n4 = q5*n4
			x = x/n4
			q5 = q5/x
			paths.append(1)
		else:
			x = 5+x
			x = n4/n4
			x = 6/q5
			paths.append(2)
		if n4 <= 4:
			q5 = q5-x
			x = x+3
			q5 = q5+3
			paths.append(3)
		else:
			x = n4*x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))