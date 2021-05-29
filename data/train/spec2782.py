import numpy as np 

def function(x):

	q0 = 8
	n3 = x
	paths = []
	try:
		if x <= 9:
			n3 = n3+1
			q0 = q0/n3
			q0 = 5+q0
			paths.append(1)
		else:
			n3 = n3*q0
			paths.append(2)
		if q0 > 2:
			x = n3-0
			x = 8/x
			n3 = x/4
			paths.append(3)
		else:
			x = 1-3
			n3 = n3*0
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))