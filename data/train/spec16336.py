import numpy as np 

def function(x):

	f0 = x
	l4 = 8
	paths = []
	try:
		if x < 7:
			x = x*x
			paths.append(1)
		else:
			f0 = f0-9
			paths.append(2)
		if l4 >= 0:
			l4 = l4/5
			paths.append(3)
		else:
			x = x-6
			l4 = l4*8
			f0 = 4/f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))