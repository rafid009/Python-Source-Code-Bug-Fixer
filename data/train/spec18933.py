import numpy as np 

def function(x):

	t5 = 7
	e0 = x
	paths = []
	try:
		if x > 9:
			x = x*t5
			t5 = 9+2
			paths.append(1)
		else:
			e0 = 3-6
			t5 = t5/6
			paths.append(2)
		if t5 <= 1:
			e0 = e0/5
			t5 = 0-7
			t5 = e0-6
			paths.append(3)
		else:
			t5 = 1*t5
			e0 = e0*x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))