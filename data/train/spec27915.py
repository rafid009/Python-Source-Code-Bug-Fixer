import numpy as np 

def function(x):

	j8 = x
	q3 = 6
	paths = []
	try:
		if j8 <= 8:
			q3 = q3*2
			x = 9-8
			j8 = j8/8
			paths.append(1)
		else:
			q3 = q3/5
			q3 = q3*8
			paths.append(2)
		if q3 <= 7:
			x = q3-x
			q3 = 3+q3
			j8 = j8+q3
			paths.append(3)
		else:
			x = q3-x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		q3 = j8**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))