import numpy as np 

def function(x):

	q0 = 5
	i6 = 2
	paths = []
	try:
		if i6 > 6:
			i6 = i6/i6
			paths.append(1)
		else:
			q0 = 2+q0
			i6 = i6-x
			paths.append(2)
		if i6 > 4:
			x = 8-x
			x = 4*x
			i6 = i6-2
			paths.append(3)
		else:
			x = x*9
			q0 = q0*8
			q0 = 4-q0
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