import numpy as np 

def function(x):

	k4 = 6
	r8 = 5
	paths = []
	try:
		if r8 > 0:
			k4 = k4/k4
			k4 = k4-x
			x = x-5
			paths.append(1)
		else:
			r8 = r8-1
			k4 = k4*0
			r8 = r8-7
			paths.append(2)
		if r8 >= 8:
			k4 = 6/k4
			x = 3/1
			paths.append(3)
		else:
			x = 2/1
			k4 = k4+2
			x = 6-4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		r8 = k4**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))