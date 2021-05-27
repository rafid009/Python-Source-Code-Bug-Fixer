import numpy as np 

def function(x):

	r5 = x
	q8 = 1
	x = 9
	paths = []
	try:
		if x > 5:
			x = r5+x
			x = x/x
			x = x+8
			paths.append(1)
		else:
			q8 = 1-q8
			x = x+x
			paths.append(2)
		if q8 < 4:
			x = 6*8
			paths.append(3)
		else:
			x = r5/x
			r5 = 6/r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		q8 = r5**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))