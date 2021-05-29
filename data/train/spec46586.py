import numpy as np 

def function(x):

	b7 = x
	e9 = 7
	paths = []
	try:
		if e9 <= 0:
			e9 = x*e9
			e9 = e9+5
			paths.append(1)
		else:
			x = 7-b7
			e9 = b7*e9
			b7 = e9+b7
			paths.append(2)
		if x <= 1:
			b7 = b7+1
			e9 = e9+x
			x = x/5
			paths.append(3)
		else:
			x = 0/5
			x = e9+x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		b7 = e9**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))