import numpy as np 

def function(x):

	q4 = x
	f9 = 2
	x = x
	paths = []
	try:
		if f9 < 0:
			f9 = x*5
			f9 = f9+9
			paths.append(1)
		else:
			f9 = 0-x
			paths.append(2)
		if f9 > 5:
			q4 = 6-x
			paths.append(3)
		else:
			x = f9+x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		q4 = f9**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))