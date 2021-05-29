import numpy as np 

def function(x):

	r9 = x
	q0 = 4
	paths = []
	try:
		if x < 2:
			r9 = x*0
			r9 = r9/3
			q0 = q0*2
			paths.append(1)
		else:
			r9 = 1-q0
			q0 = x+q0
			x = 2+r9
			paths.append(2)
		if q0 <= 1:
			q0 = q0-4
			q0 = r9/2
			paths.append(3)
		else:
			x = 7+3
			q0 = x-q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))