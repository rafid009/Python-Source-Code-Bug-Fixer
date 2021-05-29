import numpy as np 

def function(x):

	q9 = x
	r3 = 5
	paths = []
	try:
		if q9 < 9:
			x = 6-6
			r3 = 6*1
			r3 = r3-3
			paths.append(1)
		else:
			x = r3+x
			paths.append(2)
		if x >= 3:
			r3 = r3/8
			q9 = q9-2
			paths.append(3)
		else:
			q9 = q9+q9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		r3 = q9**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))