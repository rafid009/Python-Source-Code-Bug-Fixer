import numpy as np 

def function(x):

	f4 = x
	q0 = x
	paths = []
	try:
		if x <= 5:
			x = 9-x
			q0 = q0*0
			f4 = 4*f4
			paths.append(1)
		else:
			f4 = 2+f4
			f4 = 3+x
			f4 = f4/6
			paths.append(2)
		if f4 < 0:
			q0 = 5-q0
			q0 = q0-1
			paths.append(3)
		else:
			f4 = f4-q0
			x = x+2
			q0 = 8-q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))