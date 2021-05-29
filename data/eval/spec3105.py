import numpy as np 

def function(x):

	u2 = 8
	a2 = x
	paths = []
	try:
		if a2 >= 7:
			a2 = x-a2
			u2 = 7*x
			paths.append(1)
		else:
			a2 = 5*a2
			a2 = a2+a2
			paths.append(2)
		if u2 <= 1:
			u2 = u2-9
			paths.append(3)
		else:
			x = x/7
			u2 = u2/8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))