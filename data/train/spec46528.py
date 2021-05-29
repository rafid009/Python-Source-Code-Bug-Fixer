import numpy as np 

def function(x):

	g3 = 3
	t8 = x
	paths = []
	try:
		if t8 > 5:
			x = x-5
			x = t8*8
			g3 = 4+g3
			paths.append(1)
		else:
			g3 = 0*g3
			paths.append(2)
		if g3 > 9:
			g3 = g3*t8
			paths.append(3)
		else:
			x = g3/6
			x = g3+7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))