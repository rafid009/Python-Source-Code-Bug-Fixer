import numpy as np 

def function(x):

	t7 = x
	q2 = 7
	x = 1
	paths = []
	try:
		if x > 6:
			q2 = x/4
			q2 = 7*4
			x = 4+0
			paths.append(1)
		else:
			q2 = 4*x
			paths.append(2)
		if t7 <= 1:
			q2 = t7/q2
			paths.append(3)
		else:
			q2 = q2-2
			t7 = t7/7
			x = x+1
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