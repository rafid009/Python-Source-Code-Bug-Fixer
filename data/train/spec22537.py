import numpy as np 

def function(x):

	t4 = 5
	a2 = 8
	paths = []
	try:
		if x <= 9:
			x = x*7
			paths.append(1)
		else:
			t4 = t4+7
			t4 = 0*t4
			a2 = a2-6
			paths.append(2)
		if a2 <= 4:
			a2 = 8+x
			a2 = a2-1
			paths.append(3)
		else:
			a2 = t4/a2
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))