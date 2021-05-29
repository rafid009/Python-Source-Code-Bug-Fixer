import numpy as np 

def function(x):

	q0 = x
	j6 = 4
	paths = []
	try:
		if j6 > 9:
			q0 = q0*5
			x = x-0
			q0 = q0+1
			paths.append(1)
		else:
			x = 9+j6
			j6 = j6-3
			paths.append(2)
		if x >= 9:
			x = x*x
			j6 = x*q0
			paths.append(3)
		else:
			x = 0-x
			q0 = 7-5
			x = q0*1
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		j6 = q0**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))