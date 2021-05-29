import numpy as np 

def function(x):

	t2 = 3
	a1 = 1
	paths = []
	try:
		if x < 8:
			x = 8/x
			t2 = t2-5
			x = 1-x
			paths.append(1)
		else:
			t2 = t2-9
			x = a1-a1
			paths.append(2)
		if t2 > 6:
			a1 = a1*2
			paths.append(3)
		else:
			a1 = x/a1
			x = x-5
			t2 = 4+x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))