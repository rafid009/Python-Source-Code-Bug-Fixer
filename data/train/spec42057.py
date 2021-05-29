import numpy as np 

def function(x):

	q4 = x
	k2 = 9
	paths = []
	try:
		if k2 > 5:
			k2 = x*4
			q4 = q4+k2
			q4 = q4*2
			paths.append(1)
		else:
			x = 8+x
			k2 = 4/4
			paths.append(2)
		if k2 > 3:
			q4 = q4+k2
			q4 = 8+q4
			paths.append(3)
		else:
			k2 = k2/x
			x = x/6
			k2 = q4-k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))