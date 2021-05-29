import numpy as np 

def function(x):

	g1 = x
	f7 = x
	x = 5
	paths = []
	try:
		if g1 <= 2:
			g1 = g1+9
			f7 = 9/1
			paths.append(1)
		else:
			f7 = g1-f7
			g1 = 5*8
			paths.append(2)
		if x <= 3:
			g1 = g1*1
			paths.append(3)
		else:
			g1 = x/g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))