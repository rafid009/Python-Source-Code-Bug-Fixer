import numpy as np 

def function(x):

	o0 = 0
	q9 = 5
	paths = []
	try:
		if x <= 3:
			o0 = 3/q9
			paths.append(1)
		else:
			o0 = o0+1
			paths.append(2)
		if q9 > 2:
			o0 = o0/x
			paths.append(3)
		else:
			o0 = x+o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		q9 = o0**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))