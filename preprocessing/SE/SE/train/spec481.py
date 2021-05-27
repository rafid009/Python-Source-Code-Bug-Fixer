import numpy as np 

def function(x):

	q2 = 0
	u3 = 9
	paths = []
	try:
		if q2 >= 7:
			q2 = q2*9
			x = 4-x
			paths.append(1)
		else:
			u3 = 8+7
			x = q2/x
			paths.append(2)
		if u3 < 3:
			x = q2+1
			q2 = 0*x
			x = 2/x
			paths.append(3)
		else:
			x = u3/1
			x = x-8
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))