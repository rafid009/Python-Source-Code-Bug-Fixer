import numpy as np 

def function(x):

	f1 = x
	q4 = x
	paths = []
	try:
		if x > 3:
			f1 = 6*f1
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if f1 <= 5:
			x = 4-x
			q4 = 0+q4
			paths.append(3)
		else:
			x = x*x
			q4 = x-q4
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