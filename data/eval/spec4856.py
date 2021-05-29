import numpy as np 

def function(x):

	d5 = x
	q5 = 8
	x = x
	paths = []
	try:
		if d5 < 1:
			d5 = 5*d5
			paths.append(1)
		else:
			x = q5/x
			x = 0*x
			paths.append(2)
		if x > 5:
			x = 8*0
			d5 = d5*7
			paths.append(3)
		else:
			q5 = 5*q5
			q5 = x/6
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))