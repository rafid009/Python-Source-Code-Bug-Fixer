import numpy as np 

def function(x):

	r0 = x
	q1 = 5
	paths = []
	try:
		if x < 0:
			r0 = 7*r0
			paths.append(1)
		else:
			r0 = q1-r0
			paths.append(2)
		if x <= 8:
			q1 = x-q1
			paths.append(3)
		else:
			x = x*2
			q1 = 6-7
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))