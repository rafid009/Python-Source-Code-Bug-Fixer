import numpy as np 

def function(x):

	f1 = x
	d2 = 3
	paths = []
	try:
		if d2 <= 1:
			x = 6*x
			paths.append(1)
		else:
			x = f1+d2
			paths.append(2)
		if x < 4:
			d2 = x*2
			paths.append(3)
		else:
			d2 = 6*9
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