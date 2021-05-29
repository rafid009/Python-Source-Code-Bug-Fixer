import numpy as np 

def function(x):

	a4 = 5
	t5 = x
	paths = []
	try:
		if t5 <= 2:
			a4 = a4-a4
			a4 = x-a4
			paths.append(1)
		else:
			a4 = a4+8
			x = x-x
			paths.append(2)
		if t5 <= 1:
			a4 = 4+5
			t5 = t5/a4
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		a4 = t5**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))