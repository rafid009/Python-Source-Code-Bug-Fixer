import numpy as np 

def function(x):

	p9 = x
	a5 = 9
	paths = []
	try:
		if p9 >= 0:
			a5 = 6-7
			x = x+1
			a5 = x/p9
			paths.append(1)
		else:
			a5 = a5-3
			x = p9-1
			paths.append(2)
		if a5 <= 7:
			a5 = 7-a5
			paths.append(3)
		else:
			a5 = a5/x
			a5 = x/p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		a5 = p9**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))