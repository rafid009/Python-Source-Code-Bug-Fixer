import numpy as np 

def function(x):

	b1 = x
	t1 = 9
	paths = []
	try:
		if x <= 5:
			x = x*t1
			x = 6+0
			x = 4+7
			paths.append(1)
		else:
			b1 = b1+x
			t1 = 5+t1
			t1 = 5-t1
			paths.append(2)
		if x < 6:
			x = t1+3
			b1 = b1+t1
			x = x-8
			paths.append(3)
		else:
			b1 = b1+2
			x = 2+t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))