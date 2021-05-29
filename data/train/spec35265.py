import numpy as np 

def function(x):

	b2 = x
	t1 = 9
	paths = []
	try:
		if x > 5:
			x = t1-x
			b2 = 6+x
			paths.append(1)
		else:
			b2 = 9*b2
			b2 = x*3
			x = x+t1
			paths.append(2)
		if t1 < 7:
			b2 = b2-2
			t1 = t1*x
			paths.append(3)
		else:
			b2 = b2/8
			x = x*4
			b2 = 4+b2
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