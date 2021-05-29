import numpy as np 

def function(x):

	a3 = 0
	t8 = 9
	paths = []
	try:
		if a3 > 2:
			a3 = 5-7
			paths.append(1)
		else:
			a3 = a3-a3
			x = 5-x
			a3 = a3/t8
			paths.append(2)
		if a3 > 2:
			x = 2+x
			a3 = 7*a3
			paths.append(3)
		else:
			t8 = 6-5
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))