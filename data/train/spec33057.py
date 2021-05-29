import numpy as np 

def function(x):

	q0 = x
	f0 = 3
	paths = []
	try:
		if f0 > 9:
			f0 = f0-q0
			x = x+7
			paths.append(1)
		else:
			f0 = 0-f0
			q0 = 8/x
			paths.append(2)
		if x < 7:
			x = f0+x
			paths.append(3)
		else:
			x = 4-x
			f0 = f0*6
			q0 = q0/9
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		q0 = f0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))