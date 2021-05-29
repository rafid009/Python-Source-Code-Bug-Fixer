import numpy as np 

def function(x):

	t9 = x
	a3 = 7
	paths = []
	try:
		if t9 >= 9:
			t9 = 1+t9
			paths.append(1)
		else:
			t9 = t9*x
			x = 5/5
			t9 = 3+a3
			paths.append(2)
		if x > 9:
			t9 = 7-a3
			paths.append(3)
		else:
			a3 = a3-t9
			t9 = a3/t9
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))