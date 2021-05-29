import numpy as np 

def function(x):

	w4 = 0
	q9 = x
	paths = []
	try:
		if w4 > 5:
			x = 0-x
			paths.append(1)
		else:
			w4 = w4*0
			w4 = 0*w4
			paths.append(2)
		if w4 > 6:
			x = x-2
			x = x+w4
			w4 = w4*8
			paths.append(3)
		else:
			w4 = 4+x
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