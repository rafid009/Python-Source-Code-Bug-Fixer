import numpy as np 

def function(x):

	l5 = 2
	f0 = x
	paths = []
	try:
		if x > 9:
			x = 4*l5
			paths.append(1)
		else:
			f0 = 5/f0
			f0 = x+f0
			paths.append(2)
		if x <= 6:
			l5 = l5+1
			l5 = 4*4
			paths.append(3)
		else:
			l5 = 1/l5
			l5 = l5*4
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