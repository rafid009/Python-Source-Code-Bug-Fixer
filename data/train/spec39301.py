import numpy as np 

def function(x):

	q3 = x
	d5 = 7
	x = 2
	paths = []
	try:
		if d5 <= 5:
			x = d5+4
			q3 = 6*0
			x = 9/q3
			paths.append(1)
		else:
			q3 = q3-9
			q3 = q3+9
			paths.append(2)
		if q3 < 7:
			d5 = d5+q3
			paths.append(3)
		else:
			d5 = 5/d5
			x = q3*q3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))