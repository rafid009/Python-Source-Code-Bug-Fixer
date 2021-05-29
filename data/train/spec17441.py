import numpy as np 

def function(x):

	q2 = 1
	f1 = 4
	paths = []
	try:
		if x <= 0:
			f1 = f1*8
			x = 9/x
			paths.append(1)
		else:
			q2 = q2*7
			f1 = f1-q2
			paths.append(2)
		if q2 > 0:
			f1 = 2/f1
			x = x/f1
			x = 3/x
			paths.append(3)
		else:
			x = x-x
			f1 = 4-0
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))