import numpy as np 

def function(x):

	q3 = x
	v9 = 6
	paths = []
	try:
		if x >= 7:
			v9 = v9*9
			x = x+q3
			paths.append(1)
		else:
			x = v9/5
			x = x*1
			paths.append(2)
		if q3 > 9:
			x = x/9
			v9 = 9/v9
			v9 = v9+3
			paths.append(3)
		else:
			v9 = v9/2
			q3 = q3+8
			v9 = x/v9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))