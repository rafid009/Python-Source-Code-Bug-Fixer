import numpy as np 

def function(x):

	t3 = x
	a0 = 5
	paths = []
	try:
		if t3 < 3:
			x = x*a0
			a0 = a0-0
			paths.append(1)
		else:
			x = x-3
			a0 = a0-9
			x = 6/2
			paths.append(2)
		if x > 2:
			x = x-1
			a0 = x-7
			t3 = a0-t3
			paths.append(3)
		else:
			t3 = t3+8
			t3 = t3*0
			t3 = 9-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))