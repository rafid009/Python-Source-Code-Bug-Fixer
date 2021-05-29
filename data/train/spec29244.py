import numpy as np 

def function(x):

	b1 = x
	e2 = 3
	paths = []
	try:
		if e2 > 4:
			e2 = e2-0
			e2 = x/x
			x = b1*b1
			paths.append(1)
		else:
			x = x+8
			x = 6+5
			e2 = e2+4
			paths.append(2)
		if b1 < 8:
			b1 = 3*b1
			b1 = 5-b1
			e2 = e2-9
			paths.append(3)
		else:
			b1 = 3/b1
			b1 = 8/e2
			e2 = e2+b1
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		b1 = e2**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))