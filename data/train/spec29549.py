import numpy as np 

def function(x):

	f3 = x
	d2 = 8
	paths = []
	try:
		if x >= 4:
			x = 9*x
			x = 0-d2
			d2 = d2*9
			paths.append(1)
		else:
			x = 7*2
			paths.append(2)
		if x <= 3:
			x = x-9
			paths.append(3)
		else:
			f3 = d2+f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))