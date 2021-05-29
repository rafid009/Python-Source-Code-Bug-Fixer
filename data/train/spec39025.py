import numpy as np 

def function(x):

	f1 = 2
	l7 = x
	x = 3
	paths = []
	try:
		if l7 < 5:
			x = 0-x
			f1 = x/x
			l7 = x*2
			paths.append(1)
		else:
			l7 = l7-7
			paths.append(2)
		if f1 < 3:
			f1 = l7*f1
			paths.append(3)
		else:
			x = x+8
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