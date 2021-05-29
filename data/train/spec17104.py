import numpy as np 

def function(x):

	r8 = 1
	a4 = 9
	paths = []
	try:
		if a4 >= 4:
			a4 = a4/x
			x = x*6
			paths.append(1)
		else:
			a4 = 7-a4
			r8 = 7*0
			paths.append(2)
		if x <= 9:
			x = x*8
			x = x*a4
			x = x/a4
			paths.append(3)
		else:
			a4 = a4-9
			a4 = 5/a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))