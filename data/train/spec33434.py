import numpy as np 

def function(x):

	q5 = x
	o4 = x
	paths = []
	try:
		if q5 <= 3:
			o4 = o4-3
			x = q5+x
			x = 2-x
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if o4 >= 9:
			q5 = 9+q5
			x = q5+q5
			o4 = o4+o4
			paths.append(3)
		else:
			o4 = o4*1
			x = 0*x
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