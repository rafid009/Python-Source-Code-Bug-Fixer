import numpy as np 

def function(x):

	e1 = x
	k9 = 8
	paths = []
	try:
		if e1 >= 0:
			e1 = 9*e1
			x = 3*x
			paths.append(1)
		else:
			x = e1/8
			k9 = k9+3
			x = 5+x
			paths.append(2)
		if e1 < 4:
			k9 = k9/k9
			e1 = e1/1
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		k9 = e1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))