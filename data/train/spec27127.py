import numpy as np 

def function(x):

	b6 = x
	r3 = 9
	paths = []
	try:
		if r3 < 5:
			b6 = b6*6
			paths.append(1)
		else:
			r3 = 9*x
			x = 0+x
			paths.append(2)
		if r3 >= 9:
			r3 = r3+r3
			r3 = b6-5
			r3 = r3/4
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		b6 = r3**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))