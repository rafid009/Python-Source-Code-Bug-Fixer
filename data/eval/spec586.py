import numpy as np 

def function(x):

	b2 = x
	e9 = x
	paths = []
	try:
		if x <= 9:
			b2 = b2/1
			x = 6+2
			e9 = e9+1
			paths.append(1)
		else:
			e9 = e9*8
			x = x/b2
			paths.append(2)
		if e9 > 1:
			e9 = 7/7
			e9 = e9/7
			b2 = b2-3
			paths.append(3)
		else:
			x = 5+2
			x = x*9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		b2 = e9**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))