import numpy as np 

def function(x):

	q3 = 2
	k7 = 8
	paths = []
	try:
		if q3 <= 5:
			k7 = k7-q3
			k7 = 5-k7
			k7 = x/7
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if q3 <= 9:
			k7 = k7*q3
			q3 = q3+x
			k7 = k7+9
			paths.append(3)
		else:
			x = x*q3
			x = x/9
			k7 = 2+k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))