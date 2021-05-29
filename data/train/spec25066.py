import numpy as np 

def function(x):

	q4 = x
	w5 = 5
	paths = []
	try:
		if x < 8:
			w5 = q4/8
			paths.append(1)
		else:
			x = x-x
			w5 = w5*6
			q4 = 8*q4
			paths.append(2)
		if q4 <= 5:
			x = x-x
			w5 = w5/9
			paths.append(3)
		else:
			q4 = x*x
			q4 = x*0
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))