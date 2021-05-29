import numpy as np 

def function(x):

	q0 = 4
	f0 = x
	paths = []
	try:
		if x > 2:
			x = 8+x
			x = x*6
			q0 = 3-q0
			paths.append(1)
		else:
			f0 = f0+3
			f0 = f0*6
			x = x+0
			paths.append(2)
		if f0 > 5:
			f0 = f0-2
			paths.append(3)
		else:
			q0 = q0*2
			q0 = 1*q0
			q0 = x/q0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))