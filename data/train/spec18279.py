import numpy as np 

def function(x):

	r5 = x
	q0 = x
	paths = []
	try:
		if x <= 3:
			q0 = x*q0
			paths.append(1)
		else:
			x = x/x
			x = x/7
			x = x/6
			paths.append(2)
		if x <= 3:
			r5 = r5-8
			paths.append(3)
		else:
			r5 = r5+x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		q0 = r5**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))