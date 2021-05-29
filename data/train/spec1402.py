import numpy as np 

def function(x):

	q4 = x
	x5 = x
	paths = []
	try:
		if q4 < 9:
			x5 = q4*7
			paths.append(1)
		else:
			x = 4-7
			x5 = q4/x5
			x = x/9
			paths.append(2)
		if q4 > 0:
			x = 9+x
			q4 = 6+2
			q4 = 7+0
			paths.append(3)
		else:
			x5 = q4*0
			x5 = 5+q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x5 = q4**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))