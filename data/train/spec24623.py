import numpy as np 

def function(x):

	y5 = x
	q0 = x
	paths = []
	try:
		if x < 4:
			y5 = 5-y5
			y5 = q0*y5
			y5 = x/9
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if q0 > 7:
			x = 2+x
			q0 = q0*3
			paths.append(3)
		else:
			x = 6/3
			x = x+0
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		q0 = y5**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))