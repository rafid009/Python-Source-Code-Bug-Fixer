import numpy as np 

def function(x):

	q1 = 6
	f6 = x
	paths = []
	try:
		if x >= 5:
			x = x/2
			q1 = f6-1
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if x > 4:
			x = 4-q1
			x = 3+x
			q1 = 3/q1
			paths.append(3)
		else:
			q1 = q1-3
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))