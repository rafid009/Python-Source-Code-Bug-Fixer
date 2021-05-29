import numpy as np 

def function(x):

	b5 = x
	t1 = x
	paths = []
	try:
		if t1 < 1:
			b5 = 1/2
			t1 = t1+9
			paths.append(1)
		else:
			x = b5*x
			paths.append(2)
		if b5 <= 2:
			b5 = 6+b5
			b5 = 1-1
			b5 = b5/5
			paths.append(3)
		else:
			x = 5*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))