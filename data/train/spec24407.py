import numpy as np 

def function(x):

	e6 = x
	f1 = 5
	paths = []
	try:
		if f1 >= 3:
			x = x-8
			x = x+x
			f1 = x*0
			paths.append(1)
		else:
			e6 = 4/e6
			x = 9/f1
			e6 = e6+3
			paths.append(2)
		if f1 >= 6:
			x = x*f1
			paths.append(3)
		else:
			f1 = e6-f1
			x = f1*x
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