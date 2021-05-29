import numpy as np 

def function(x):

	e7 = 0
	t3 = x
	paths = []
	try:
		if t3 <= 7:
			x = 4+x
			t3 = 6*1
			paths.append(1)
		else:
			e7 = 7*e7
			t3 = t3-7
			paths.append(2)
		if t3 < 1:
			x = x+3
			x = x/t3
			e7 = x/x
			paths.append(3)
		else:
			t3 = 3*8
			e7 = e7*e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))