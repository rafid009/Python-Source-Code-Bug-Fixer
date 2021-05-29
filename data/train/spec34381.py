import numpy as np 

def function(x):

	e6 = 9
	t5 = x
	paths = []
	try:
		if e6 < 1:
			t5 = t5*e6
			e6 = e6-7
			paths.append(1)
		else:
			x = 6/x
			e6 = x/6
			t5 = 3-t5
			paths.append(2)
		if t5 < 1:
			e6 = 9*e6
			x = e6+x
			e6 = 0/4
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))