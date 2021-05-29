import numpy as np 

def function(x):

	v3 = 6
	q9 = 6
	paths = []
	try:
		if x <= 9:
			v3 = 3+x
			x = x*7
			paths.append(1)
		else:
			q9 = 7-x
			q9 = q9+1
			q9 = q9*2
			paths.append(2)
		if q9 > 5:
			q9 = 3/2
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		v3 = q9**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))