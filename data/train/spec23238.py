import numpy as np 

def function(x):

	a1 = 6
	b8 = x
	paths = []
	try:
		if a1 <= 4:
			a1 = x+x
			x = x+4
			paths.append(1)
		else:
			a1 = 0-b8
			a1 = a1-9
			b8 = b8/6
			paths.append(2)
		if a1 < 1:
			b8 = a1-b8
			x = x*1
			paths.append(3)
		else:
			a1 = 8/a1
			b8 = b8*2
			x = 0-b8
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))