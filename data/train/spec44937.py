import numpy as np 

def function(x):

	u7 = 5
	q0 = 4
	paths = []
	try:
		if q0 > 2:
			u7 = x/q0
			u7 = x*u7
			x = 0-2
			paths.append(1)
		else:
			q0 = q0/1
			x = x-5
			x = 2*2
			paths.append(2)
		if u7 >= 6:
			x = 4+u7
			q0 = 2+x
			u7 = 1+q0
			paths.append(3)
		else:
			u7 = 6+3
			u7 = u7/2
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