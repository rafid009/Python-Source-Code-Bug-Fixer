import numpy as np 

def function(x):

	q2 = x
	w5 = 7
	paths = []
	try:
		if q2 <= 2:
			w5 = 8/w5
			w5 = q2*w5
			paths.append(1)
		else:
			w5 = 8*w5
			w5 = q2*6
			w5 = w5*1
			paths.append(2)
		if q2 > 5:
			q2 = q2*1
			q2 = q2+6
			paths.append(3)
		else:
			x = x-6
			q2 = 1+0
			x = x+5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		q2 = w5**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))