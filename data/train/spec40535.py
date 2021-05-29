import numpy as np 

def function(x):

	v1 = x
	q0 = 3
	paths = []
	try:
		if x < 4:
			x = x-8
			paths.append(1)
		else:
			x = 2+x
			q0 = 2-q0
			q0 = q0*2
			paths.append(2)
		if v1 > 8:
			x = q0/x
			q0 = x*v1
			paths.append(3)
		else:
			q0 = q0*4
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		v1 = q0**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))