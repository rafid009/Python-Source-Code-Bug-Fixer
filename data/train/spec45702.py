import numpy as np 

def function(x):

	r5 = 0
	q5 = 7
	paths = []
	try:
		if r5 < 7:
			r5 = r5/5
			r5 = r5*r5
			paths.append(1)
		else:
			x = 0/x
			q5 = q5*4
			q5 = q5+6
			paths.append(2)
		if q5 <= 8:
			q5 = q5+q5
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))