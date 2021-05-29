import numpy as np 

def function(x):

	q9 = 7
	i7 = x
	paths = []
	try:
		if i7 < 5:
			i7 = i7*1
			paths.append(1)
		else:
			q9 = 9/q9
			x = q9+3
			paths.append(2)
		if x > 8:
			i7 = i7-i7
			paths.append(3)
		else:
			x = q9*4
			x = x*6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		q9 = i7**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))