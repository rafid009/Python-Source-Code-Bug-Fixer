import numpy as np 

def function(x):

	q7 = x
	t1 = x
	paths = []
	try:
		if x > 3:
			q7 = 2-q7
			q7 = 5-q7
			q7 = t1*q7
			paths.append(1)
		else:
			q7 = 8*2
			q7 = 0-1
			x = 3-2
			paths.append(2)
		if x < 2:
			x = x*1
			paths.append(3)
		else:
			x = x*8
			q7 = q7+0
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		t1 = q7**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))