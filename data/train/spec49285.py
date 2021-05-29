import numpy as np 

def function(x):

	t5 = x
	d9 = x
	paths = []
	try:
		if t5 > 2:
			t5 = x*x
			t5 = 3+7
			paths.append(1)
		else:
			x = x+3
			d9 = 6*2
			t5 = 8/t5
			paths.append(2)
		if t5 <= 9:
			d9 = 2-d9
			d9 = d9/d9
			x = x*d9
			paths.append(3)
		else:
			t5 = t5*d9
			t5 = 5*t5
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