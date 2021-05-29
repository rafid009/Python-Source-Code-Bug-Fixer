import numpy as np 

def function(x):

	q5 = x
	j3 = x
	paths = []
	try:
		if q5 <= 9:
			x = 5/j3
			j3 = j3+8
			paths.append(1)
		else:
			j3 = j3*7
			paths.append(2)
		if j3 > 6:
			j3 = 8*j3
			paths.append(3)
		else:
			q5 = 9+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))