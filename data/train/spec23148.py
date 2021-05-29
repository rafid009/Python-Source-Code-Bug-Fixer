import numpy as np 

def function(x):

	q2 = x
	u1 = x
	paths = []
	try:
		if u1 > 3:
			x = x+3
			q2 = q2*2
			q2 = q2+1
			paths.append(1)
		else:
			u1 = q2-7
			u1 = u1+6
			u1 = x-u1
			paths.append(2)
		if x < 9:
			x = x-7
			u1 = u1-1
			paths.append(3)
		else:
			q2 = 1-7
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))