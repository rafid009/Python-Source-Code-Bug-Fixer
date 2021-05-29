import numpy as np 

def function(x):

	f6 = x
	q0 = 9
	paths = []
	try:
		if q0 <= 3:
			q0 = q0+9
			paths.append(1)
		else:
			q0 = f6/7
			q0 = q0/1
			x = x-4
			paths.append(2)
		if x >= 2:
			f6 = f6+1
			f6 = q0/f6
			q0 = q0*0
			paths.append(3)
		else:
			f6 = f6*x
			q0 = 8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))