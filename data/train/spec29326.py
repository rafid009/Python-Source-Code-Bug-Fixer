import numpy as np 

def function(x):

	f1 = x
	q6 = x
	paths = []
	try:
		if x >= 4:
			x = x*2
			x = x/4
			paths.append(1)
		else:
			q6 = q6+9
			f1 = f1+3
			f1 = 3*6
			paths.append(2)
		if x < 6:
			x = x+4
			f1 = 7-f1
			paths.append(3)
		else:
			q6 = q6+6
			q6 = q6/x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		q6 = f1**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))