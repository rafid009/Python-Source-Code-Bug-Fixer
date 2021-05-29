import numpy as np 

def function(x):

	q8 = 4
	v6 = 6
	paths = []
	try:
		if v6 < 7:
			q8 = q8-5
			v6 = 2+x
			v6 = 9-v6
			paths.append(1)
		else:
			q8 = q8+x
			q8 = q8-q8
			x = 6+q8
			paths.append(2)
		if q8 >= 3:
			q8 = 9-x
			paths.append(3)
		else:
			v6 = 5*7
			v6 = v6-x
			x = q8*x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))