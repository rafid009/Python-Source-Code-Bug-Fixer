import numpy as np 

def function(x):

	w5 = 9
	a4 = x
	paths = []
	try:
		if a4 > 6:
			a4 = x-2
			x = 7+7
			a4 = a4-9
			paths.append(1)
		else:
			a4 = 7+9
			a4 = 3*a4
			a4 = a4*9
			paths.append(2)
		if a4 <= 3:
			x = x/a4
			x = a4*x
			paths.append(3)
		else:
			x = x*2
			w5 = w5-5
			x = x+a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))