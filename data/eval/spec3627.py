import numpy as np 

def function(x):

	q5 = x
	n4 = x
	paths = []
	try:
		if x <= 4:
			n4 = q5*q5
			paths.append(1)
		else:
			x = 3*2
			x = 9/x
			q5 = q5+9
			paths.append(2)
		if q5 >= 9:
			n4 = n4-q5
			q5 = 1*5
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		n4 = q5**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))