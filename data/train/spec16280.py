import numpy as np 

def function(x):

	a2 = x
	r1 = x
	paths = []
	try:
		if r1 <= 6:
			r1 = r1+1
			x = r1*9
			x = x/8
			paths.append(1)
		else:
			x = x+7
			x = 9+a2
			paths.append(2)
		if a2 <= 3:
			a2 = x-3
			a2 = 9-7
			paths.append(3)
		else:
			a2 = r1+a2
			a2 = 8-a2
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))