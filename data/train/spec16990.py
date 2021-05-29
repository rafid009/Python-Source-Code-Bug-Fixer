import numpy as np 

def function(x):

	f2 = x
	q2 = 3
	paths = []
	try:
		if x > 0:
			x = 3-x
			x = 6-9
			paths.append(1)
		else:
			q2 = 8+7
			q2 = 2+x
			f2 = 4-f2
			paths.append(2)
		if f2 >= 9:
			x = x/q2
			f2 = f2-f2
			q2 = x/7
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))