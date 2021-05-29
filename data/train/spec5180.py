import numpy as np 

def function(x):

	q2 = 4
	c6 = x
	paths = []
	try:
		if x < 2:
			q2 = 4+q2
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if q2 <= 9:
			x = x/7
			x = c6+8
			x = 0/q2
			paths.append(3)
		else:
			q2 = 0+c6
			q2 = q2-9
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		q2 = c6**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))