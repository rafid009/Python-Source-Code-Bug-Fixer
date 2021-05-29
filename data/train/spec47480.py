import numpy as np 

def function(x):

	t4 = 9
	b2 = x
	paths = []
	try:
		if x <= 2:
			x = b2/b2
			t4 = 1-1
			paths.append(1)
		else:
			t4 = t4+3
			b2 = 6+x
			x = 5*x
			paths.append(2)
		if x < 4:
			t4 = t4*3
			paths.append(3)
		else:
			x = x+7
			x = b2*8
			b2 = t4-5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))