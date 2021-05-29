import numpy as np 

def function(x):

	w0 = 9
	q3 = x
	x = 6
	paths = []
	try:
		if w0 >= 1:
			w0 = w0*0
			w0 = 6-8
			paths.append(1)
		else:
			x = x+q3
			w0 = w0+8
			paths.append(2)
		if q3 <= 0:
			q3 = q3*3
			q3 = 8+4
			paths.append(3)
		else:
			x = x+x
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		q3 = w0**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))