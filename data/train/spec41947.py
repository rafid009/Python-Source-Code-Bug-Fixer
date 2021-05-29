import numpy as np 

def function(x):

	q9 = x
	r9 = 4
	paths = []
	try:
		if x <= 9:
			q9 = q9*4
			x = 5/x
			paths.append(1)
		else:
			r9 = q9/r9
			paths.append(2)
		if r9 < 0:
			q9 = q9/r9
			q9 = 3-6
			paths.append(3)
		else:
			q9 = 7+x
			r9 = 9/r9
			r9 = x/7
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))