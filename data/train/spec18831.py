import numpy as np 

def function(x):

	t9 = 2
	e9 = x
	x = x
	paths = []
	try:
		if t9 > 2:
			e9 = 5*e9
			e9 = e9*0
			t9 = t9+7
			paths.append(1)
		else:
			x = 2+x
			x = e9+x
			t9 = x+5
			paths.append(2)
		if e9 <= 5:
			e9 = 1/7
			paths.append(3)
		else:
			t9 = x+6
			e9 = 8/e9
			t9 = t9/t9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))