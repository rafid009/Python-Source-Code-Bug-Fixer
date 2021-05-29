import numpy as np 

def function(x):

	q2 = 1
	r1 = x
	paths = []
	try:
		if q2 > 5:
			r1 = q2*1
			r1 = 7-r1
			paths.append(1)
		else:
			r1 = r1+q2
			paths.append(2)
		if q2 < 9:
			r1 = 2-r1
			paths.append(3)
		else:
			r1 = r1*4
			q2 = q2/9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))