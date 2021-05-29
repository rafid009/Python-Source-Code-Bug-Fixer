import numpy as np 

def function(x):

	g3 = x
	b6 = x
	paths = []
	try:
		if x < 1:
			x = x*8
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if g3 <= 6:
			x = x-x
			b6 = x*g3
			x = x/5
			paths.append(3)
		else:
			x = x/g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		b6 = g3**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))