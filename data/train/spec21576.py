import numpy as np 

def function(x):

	f2 = x
	q6 = x
	paths = []
	try:
		if f2 >= 0:
			x = 4+x
			q6 = q6*7
			f2 = x*9
			paths.append(1)
		else:
			x = q6+x
			q6 = q6+2
			paths.append(2)
		if f2 < 1:
			f2 = f2-5
			paths.append(3)
		else:
			x = 6-q6
			f2 = q6/f2
			x = x+q6
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))