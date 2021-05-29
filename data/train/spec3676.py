import numpy as np 

def function(x):

	f3 = 5
	q1 = 9
	paths = []
	try:
		if f3 <= 2:
			x = 2/6
			paths.append(1)
		else:
			q1 = q1-2
			paths.append(2)
		if f3 <= 8:
			x = x+4
			f3 = f3-8
			q1 = 5-q1
			paths.append(3)
		else:
			x = x-f3
			x = 7+x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))