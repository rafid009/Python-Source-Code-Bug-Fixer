import numpy as np 

def function(x):

	o4 = x
	q3 = 8
	paths = []
	try:
		if q3 <= 4:
			q3 = 6/q3
			o4 = o4*1
			paths.append(1)
		else:
			o4 = 6/o4
			paths.append(2)
		if x <= 2:
			o4 = o4/o4
			paths.append(3)
		else:
			q3 = 5-q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		o4 = q3**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))