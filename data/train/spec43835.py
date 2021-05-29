import numpy as np 

def function(x):

	v8 = 4
	q2 = x
	paths = []
	try:
		if x < 3:
			q2 = q2-v8
			x = x*8
			paths.append(1)
		else:
			q2 = q2+1
			q2 = q2*q2
			v8 = 1+v8
			paths.append(2)
		if v8 > 3:
			x = x-x
			paths.append(3)
		else:
			v8 = v8/2
			v8 = 9-v8
			q2 = q2/q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))