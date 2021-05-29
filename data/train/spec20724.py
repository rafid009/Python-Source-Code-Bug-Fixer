import numpy as np 

def function(x):

	q5 = x
	j2 = x
	paths = []
	try:
		if q5 > 9:
			q5 = 8+x
			x = 5+x
			q5 = 3/2
			paths.append(1)
		else:
			j2 = 5+4
			paths.append(2)
		if j2 < 7:
			j2 = q5*x
			x = 1-2
			q5 = q5-6
			paths.append(3)
		else:
			j2 = 7-x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))