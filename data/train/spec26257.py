import numpy as np 

def function(x):

	q9 = x
	o0 = 6
	x = x
	paths = []
	try:
		if q9 <= 2:
			q9 = 6*q9
			paths.append(1)
		else:
			o0 = o0/q9
			o0 = o0*3
			paths.append(2)
		if o0 < 7:
			o0 = o0/8
			x = x*x
			paths.append(3)
		else:
			q9 = q9+2
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))