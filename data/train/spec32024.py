import numpy as np 

def function(x):

	a4 = x
	f6 = 5
	paths = []
	try:
		if f6 > 5:
			f6 = 7*f6
			paths.append(1)
		else:
			a4 = 7+a4
			f6 = f6+f6
			paths.append(2)
		if f6 >= 2:
			a4 = a4+2
			paths.append(3)
		else:
			x = x*2
			f6 = 7-f6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		f6 = a4**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))