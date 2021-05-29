import numpy as np 

def function(x):

	r8 = x
	q1 = x
	paths = []
	try:
		if r8 < 5:
			r8 = r8+0
			paths.append(1)
		else:
			x = q1-q1
			paths.append(2)
		if r8 <= 7:
			r8 = r8+4
			x = x*6
			paths.append(3)
		else:
			q1 = 7*q1
			q1 = q1/q1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))