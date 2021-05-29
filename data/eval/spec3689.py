import numpy as np 

def function(x):

	f2 = x
	q6 = 6
	paths = []
	try:
		if x > 5:
			q6 = x+5
			f2 = 5*0
			q6 = q6*f2
			paths.append(1)
		else:
			q6 = q6/1
			paths.append(2)
		if x < 3:
			q6 = 2/4
			paths.append(3)
		else:
			f2 = f2+1
			q6 = q6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))