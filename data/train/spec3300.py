import numpy as np 

def function(x):

	t5 = 0
	b7 = x
	paths = []
	try:
		if t5 < 6:
			b7 = b7*2
			x = x+x
			x = x-3
			paths.append(1)
		else:
			b7 = 3-8
			t5 = t5+3
			x = x/4
			paths.append(2)
		if x < 6:
			b7 = x/b7
			x = x-3
			t5 = t5-x
			paths.append(3)
		else:
			b7 = b7*3
			b7 = 2/1
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