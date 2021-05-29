import numpy as np 

def function(x):

	q1 = x
	o3 = 5
	paths = []
	try:
		if q1 > 6:
			x = x*q1
			o3 = 7+x
			o3 = o3-9
			paths.append(1)
		else:
			o3 = 7-4
			q1 = q1-3
			x = x-o3
			paths.append(2)
		if x <= 7:
			x = 9-7
			o3 = 2+9
			paths.append(3)
		else:
			o3 = 2-o3
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))