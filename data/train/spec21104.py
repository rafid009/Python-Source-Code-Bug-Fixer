import numpy as np 

def function(x):

	u3 = x
	q4 = x
	paths = []
	try:
		if q4 > 4:
			u3 = u3+4
			u3 = 9*u3
			paths.append(1)
		else:
			q4 = q4/2
			x = 5*x
			paths.append(2)
		if u3 < 5:
			q4 = 1*4
			q4 = u3+2
			u3 = q4/x
			paths.append(3)
		else:
			x = 0+8
			u3 = 6*u3
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		u3 = q4**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))