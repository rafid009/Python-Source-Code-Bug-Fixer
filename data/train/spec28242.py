import numpy as np 

def function(x):

	u4 = x
	q5 = 3
	paths = []
	try:
		if x < 5:
			u4 = x-9
			q5 = 5*u4
			paths.append(1)
		else:
			x = 2*x
			x = 1+q5
			paths.append(2)
		if u4 < 2:
			u4 = 4*x
			paths.append(3)
		else:
			u4 = x*5
			q5 = u4-2
			x = u4+u4
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))