import numpy as np 

def function(x):

	j2 = x
	q9 = x
	paths = []
	try:
		if j2 > 0:
			q9 = 2+q9
			paths.append(1)
		else:
			q9 = 8+q9
			q9 = 1*7
			x = q9*x
			paths.append(2)
		if q9 >= 1:
			j2 = 5*j2
			paths.append(3)
		else:
			x = 0/1
			x = x-0
			q9 = q9/q9
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))