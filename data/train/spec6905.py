import numpy as np 

def function(x):

	r8 = 5
	q3 = x
	paths = []
	try:
		if q3 >= 7:
			r8 = 0/x
			r8 = r8+9
			paths.append(1)
		else:
			q3 = q3*q3
			x = x*x
			paths.append(2)
		if r8 <= 2:
			x = q3*q3
			x = x/x
			paths.append(3)
		else:
			x = 5-8
			q3 = q3-2
			q3 = 9-q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))