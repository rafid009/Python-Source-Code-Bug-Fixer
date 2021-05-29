import numpy as np 

def function(x):

	t2 = x
	g9 = x
	paths = []
	try:
		if t2 <= 5:
			t2 = 1/t2
			t2 = 2*g9
			x = t2+7
			paths.append(1)
		else:
			t2 = t2/4
			t2 = g9-t2
			paths.append(2)
		if t2 > 4:
			t2 = 8/t2
			paths.append(3)
		else:
			x = 3+t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		g9 = t2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))