import numpy as np 

def function(x):

	f2 = x
	a2 = 8
	paths = []
	try:
		if a2 < 2:
			a2 = 2-a2
			x = x*2
			paths.append(1)
		else:
			a2 = x*8
			paths.append(2)
		if x <= 5:
			x = 1*x
			paths.append(3)
		else:
			a2 = a2-0
			f2 = f2-8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))