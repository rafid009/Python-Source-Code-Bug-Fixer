import numpy as np 

def function(x):

	q6 = x
	d2 = 3
	paths = []
	try:
		if d2 < 6:
			d2 = d2+d2
			q6 = x*8
			paths.append(1)
		else:
			x = x-9
			x = 4*q6
			q6 = 7*1
			paths.append(2)
		if q6 <= 2:
			d2 = q6+d2
			x = x*x
			q6 = q6*6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		d2 = q6**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))