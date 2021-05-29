import numpy as np 

def function(x):

	b2 = 2
	t1 = 9
	paths = []
	try:
		if x < 6:
			b2 = b2-0
			b2 = 5+t1
			paths.append(1)
		else:
			t1 = t1*2
			t1 = t1-5
			paths.append(2)
		if t1 >= 8:
			b2 = x/t1
			b2 = b2*3
			paths.append(3)
		else:
			b2 = 0*2
			b2 = b2*4
			x = 0*t1
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