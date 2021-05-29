import numpy as np 

def function(x):

	e2 = 0
	t5 = 2
	paths = []
	try:
		if t5 > 7:
			x = x-6
			x = t5-x
			paths.append(1)
		else:
			t5 = 5*0
			t5 = e2*t5
			paths.append(2)
		if e2 < 5:
			t5 = x-6
			paths.append(3)
		else:
			x = x+t5
			t5 = e2*t5
			x = 7/x
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