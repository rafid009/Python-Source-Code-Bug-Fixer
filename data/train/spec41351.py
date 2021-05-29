import numpy as np 

def function(x):

	g3 = 9
	k6 = x
	paths = []
	try:
		if x < 0:
			k6 = 3/8
			k6 = k6/1
			paths.append(1)
		else:
			x = x-k6
			k6 = k6-1
			k6 = k6*8
			paths.append(2)
		if g3 >= 7:
			g3 = x/9
			g3 = g3/4
			x = x-9
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		k6 = g3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))