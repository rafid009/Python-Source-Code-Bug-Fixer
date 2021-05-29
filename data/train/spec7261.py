import numpy as np 

def function(x):

	f1 = 1
	a5 = x
	paths = []
	try:
		if x > 9:
			a5 = f1/9
			f1 = f1*2
			paths.append(1)
		else:
			a5 = a5*1
			x = 7*x
			paths.append(2)
		if x < 0:
			a5 = 7*a5
			a5 = a5/5
			paths.append(3)
		else:
			f1 = f1-a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		f1 = a5**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))