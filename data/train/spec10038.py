import numpy as np 

def function(x):

	r5 = x
	a2 = 8
	paths = []
	try:
		if r5 <= 4:
			x = x+5
			a2 = a2/5
			r5 = a2-9
			paths.append(1)
		else:
			x = 4*x
			x = x-6
			a2 = a2/8
			paths.append(2)
		if x >= 9:
			a2 = 7-a2
			x = 4+a2
			paths.append(3)
		else:
			a2 = 8/a2
			r5 = r5*9
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))