import numpy as np 

def function(x):

	t3 = x
	b7 = x
	paths = []
	try:
		if b7 > 8:
			x = x-4
			b7 = b7*2
			paths.append(1)
		else:
			x = x*5
			x = 7-2
			paths.append(2)
		if b7 < 2:
			b7 = b7-7
			t3 = x/t3
			paths.append(3)
		else:
			b7 = 9/5
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))