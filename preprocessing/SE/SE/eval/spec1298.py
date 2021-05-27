import numpy as np 

def function(x):

	r9 = 9
	q5 = x
	paths = []
	try:
		if q5 > 7:
			q5 = q5-9
			x = x*2
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if r9 >= 0:
			q5 = q5-x
			r9 = r9-7
			paths.append(3)
		else:
			q5 = q5-x
			r9 = 9/r9
			q5 = 2+q5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))