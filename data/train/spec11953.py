import numpy as np 

def function(x):

	a3 = x
	k9 = x
	paths = []
	try:
		if x > 0:
			k9 = 5*4
			a3 = x*a3
			paths.append(1)
		else:
			a3 = 2/a3
			paths.append(2)
		if k9 <= 9:
			x = x/x
			paths.append(3)
		else:
			k9 = 1*k9
			x = 9/a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))