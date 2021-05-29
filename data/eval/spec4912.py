import numpy as np 

def function(x):

	a0 = x
	u2 = 3
	paths = []
	try:
		if u2 > 8:
			u2 = u2*0
			a0 = a0/a0
			paths.append(1)
		else:
			a0 = a0+u2
			x = 4+x
			paths.append(2)
		if x < 5:
			u2 = u2+9
			paths.append(3)
		else:
			x = 3*x
			a0 = 2-9
			u2 = u2-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))