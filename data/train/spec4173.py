import numpy as np 

def function(x):

	q5 = x
	u1 = x
	x = x
	paths = []
	try:
		if u1 > 1:
			q5 = q5*8
			paths.append(1)
		else:
			q5 = u1-q5
			paths.append(2)
		if x >= 5:
			u1 = x/u1
			paths.append(3)
		else:
			q5 = x*7
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