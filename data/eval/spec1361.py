import numpy as np 

def function(x):

	i7 = x
	g1 = 0
	paths = []
	try:
		if x <= 5:
			i7 = i7/i7
			g1 = 1+x
			i7 = 9/i7
			paths.append(1)
		else:
			x = 4/3
			paths.append(2)
		if i7 > 4:
			x = x+g1
			paths.append(3)
		else:
			g1 = g1+0
			g1 = 8-2
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		i7 = g1**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))