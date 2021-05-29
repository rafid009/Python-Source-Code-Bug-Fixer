import numpy as np 

def function(x):

	f1 = x
	l2 = 2
	paths = []
	try:
		if f1 < 8:
			x = x*f1
			l2 = l2/7
			x = 2*x
			paths.append(1)
		else:
			l2 = 8+l2
			paths.append(2)
		if l2 >= 5:
			x = x/4
			l2 = l2*0
			f1 = f1-6
			paths.append(3)
		else:
			l2 = 3-3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))