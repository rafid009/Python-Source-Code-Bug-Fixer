import numpy as np 

def function(x):

	t4 = 3
	a3 = 4
	x = 7
	paths = []
	try:
		if a3 <= 1:
			a3 = a3+9
			paths.append(1)
		else:
			a3 = a3+8
			paths.append(2)
		if t4 <= 8:
			t4 = t4*0
			a3 = 2-a3
			paths.append(3)
		else:
			a3 = a3/8
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