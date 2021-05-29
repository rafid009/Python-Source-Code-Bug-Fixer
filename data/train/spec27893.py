import numpy as np 

def function(x):

	q0 = 1
	r8 = 4
	paths = []
	try:
		if r8 < 9:
			q0 = 6-x
			q0 = q0+7
			x = x*2
			paths.append(1)
		else:
			r8 = q0+r8
			paths.append(2)
		if r8 <= 1:
			x = 1/2
			r8 = 9/2
			paths.append(3)
		else:
			x = 5/x
			r8 = r8*7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		r8 = q0**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))