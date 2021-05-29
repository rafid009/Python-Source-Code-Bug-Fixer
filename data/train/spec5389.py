import numpy as np 

def function(x):

	q5 = x
	d2 = 7
	paths = []
	try:
		if x <= 1:
			x = 9-7
			d2 = q5/x
			paths.append(1)
		else:
			d2 = 6*d2
			d2 = d2+8
			x = 4*x
			paths.append(2)
		if x < 1:
			q5 = q5/8
			d2 = d2-2
			d2 = d2/d2
			paths.append(3)
		else:
			q5 = q5+q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		d2 = q5**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))