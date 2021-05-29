import numpy as np 

def function(x):

	q5 = x
	o0 = 6
	paths = []
	try:
		if q5 <= 4:
			q5 = x/8
			o0 = q5+o0
			paths.append(1)
		else:
			o0 = o0-o0
			q5 = 2*5
			q5 = q5*4
			paths.append(2)
		if q5 < 3:
			o0 = x/o0
			paths.append(3)
		else:
			q5 = 2*q5
			x = o0+5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))