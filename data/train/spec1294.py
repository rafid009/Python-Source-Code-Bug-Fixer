import numpy as np 

def function(x):

	q4 = 4
	r7 = 0
	paths = []
	try:
		if r7 >= 5:
			q4 = q4-3
			paths.append(1)
		else:
			q4 = r7*q4
			paths.append(2)
		if r7 <= 2:
			x = x*5
			q4 = 4*8
			q4 = x*0
			paths.append(3)
		else:
			r7 = 4-r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))