import numpy as np 

def function(x):

	b5 = 3
	t3 = 5
	x = 0
	paths = []
	try:
		if x >= 7:
			b5 = b5+t3
			t3 = b5/t3
			paths.append(1)
		else:
			b5 = 2/b5
			x = 0*t3
			paths.append(2)
		if t3 <= 0:
			b5 = 2/6
			b5 = b5-1
			t3 = t3+9
			paths.append(3)
		else:
			b5 = t3-8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))