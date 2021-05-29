import numpy as np 

def function(x):

	b3 = 1
	e2 = x
	paths = []
	try:
		if b3 > 7:
			b3 = 8*1
			x = 6/x
			e2 = x+e2
			paths.append(1)
		else:
			x = x*7
			b3 = 4/b3
			paths.append(2)
		if e2 <= 9:
			b3 = 6+b3
			paths.append(3)
		else:
			e2 = 9/b3
			b3 = e2/b3
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		b3 = e2**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))